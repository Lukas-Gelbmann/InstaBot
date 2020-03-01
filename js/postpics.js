console.log(process.argv)
var arguments = process.argv.slice(2);

var pictureName = arguments[0];
var caption = arguments[1];
var username = arguments[2];
var password = arguments[3];

console.log("Picture name: " + pictureName +
            "Caption: " + caption +  
            "Username: " + username + 
            "Password:" + password);

var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var _this = this;
var IgApiClient = require('../js/node_modules/instagram-private-api').IgApiClient;
var readFile = require('fs').readFile;
var promisify = require('util').promisify;
var readFileAsync = promisify(readFile);
var ig = new IgApiClient();
function login() {
    return __awaiter(this, void 0, void 0, function () {
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    // basic login-procedure
                    ig.state.generateDevice(process.env.IG_USERNAME);
                    ig.state.proxyUrl = process.env.IG_PROXY;
                    return [4 /*yield*/, ig.account.login(username, password)];
                case 1:
                    _a.sent();
                    return [2 /*return*/];
            }
        });
    });
}
(function () { return __awaiter(_this, void 0, void 0, function () {
    var path, _a, latitude, longitude, searchQuery, locations, mediaLocation, publishResult, _b, _c, _d;
    return __generator(this, function (_e) {
        switch (_e.label) {
            case 0: return [4 /*yield*/, login()];
            case 1:
                _e.sent();
                path = '../pictures/' + pictureName;
                _a = {
                    latitude: 0.0,
                    longitude: 0.0,
                    // not required
                    searchQuery: 'place'
                }, latitude = _a.latitude, longitude = _a.longitude, searchQuery = _a.searchQuery;
                return [4 /*yield*/, ig.search.location(latitude, longitude, searchQuery)];
            case 2:
                locations = _e.sent();
                mediaLocation = locations[0];
                console.log(mediaLocation);
                _c = (_b = ig.publish).photo;
                _d = {};
                return [4 /*yield*/, readFileAsync('../pictures/' + pictureName)];
            case 3: return [4 /*yield*/, _c.apply(_b, [(
                    // read the file into a Buffer
                    _d.file = _e.sent(),
                        // optional, default ''
                        _d.caption = caption,
                        _d)])];
            case 4:
                publishResult = _e.sent();
                console.log(publishResult);
                return [2 /*return*/];
        }
    });
}); })();
/**
 * Generate a usertag
 * @param name - the instagram-username
 * @param x - x coordinate (0..1)
 * @param y - y coordinate (0..1)
 */
function generateUsertagFromName(name, x, y) {
    return __awaiter(this, void 0, void 0, function () {
        var pk;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    // constrain x and y to 0..1 (0 and 1 are not supported)
                    x = clamp(x, 0.0001, 0.9999);
                    y = clamp(y, 0.0001, 0.9999);
                    return [4 /*yield*/, ig.user.searchExact(name)];
                case 1:
                    pk = (_a.sent()).pk;
                    return [2 /*return*/, {
                            user_id: pk,
                            position: [x, y]
                        }];
            }
        });
    });
}
/**
 * Constrain a value
 * @param value
 * @param min
 * @param max
 */
var clamp = function (value, min, max) { return Math.max(Math.min(value, max), min); };
