const { IgApiClient } = require('../js/node_modules/instagram-private-api');
const { readFile } = require('fs');
const { promisify } = require('util');
const readFileAsync = promisify(readFile);

const ig = new IgApiClient();

async function login() {
  // basic login-procedure
  ig.state.generateDevice(process.env.IG_USERNAME);
  ig.state.proxyUrl = process.env.IG_PROXY;
  await ig.account.login('owexactly00', 'mM9cjG9EpZaATis');
}

(async () => {
  await login();

  const path = '../pictures/test.jpg';
  const { latitude, longitude, searchQuery } = {
    latitude: 0.0,
    longitude: 0.0,
    // not required
    searchQuery: 'place',
  };

  /**
   * Get the place
   * If searchQuery is undefined, you'll get the nearest places to your location
   * this is the same as in the upload (-configure) dialog in the app
   */
  const locations = await ig.search.location(latitude, longitude, searchQuery);
  /**
   * Get the first venue
   * In the real world you would check the returned locations
   */
  const mediaLocation = locations[0];
  console.log(mediaLocation);

  const publishResult = await ig.publish.photo({
    // read the file into a Buffer
    file: await readFileAsync('../pictures/test.jpg'),
    // optional, default ''
    caption: 'moin'
    // optional
    //location: mediaLocation,
    // optional
    //usertags: {
    //  in: [
    //    // tag the user 'instagram' @ (0.5 | 0.5)
    //    await generateUsertagFromName('instagram', 0.5, 0.5),
    //  ],
    //},
  });

  console.log(publishResult);
})();

/**
 * Generate a usertag
 * @param name - the instagram-username
 * @param x - x coordinate (0..1)
 * @param y - y coordinate (0..1)
 */
async function generateUsertagFromName(name: string, x: number, y: number): Promise<{ user_id: number, position: [number, number] }> {
  // constrain x and y to 0..1 (0 and 1 are not supported)
  x = clamp(x, 0.0001, 0.9999);
  y = clamp(y, 0.0001, 0.9999);
  // get the user_id (pk) for the name
  const { pk } = await ig.user.searchExact(name);
  return {
    user_id: pk,
    position: [x, y],
  };
}

/**
 * Constrain a value
 * @param value
 * @param min
 * @param max
 */
const clamp = (value: number, min: number, max: number) => Math.max(Math.min(value, max), min);