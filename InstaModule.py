import InstagramAPI
from random import randint, seed, choice
from time import sleep
from datetime import datetime
import os
import requests
import urllib

class InstaBotFunctions:
    programpath = os.path.dirname(__file__)
    users_list = []
    following_users = []
    follower_users = []

    def __init__(self, username, password):
        global api
        api = InstagramAPI.InstagramAPI(username,password)
        api.login()

    def writeLog(self, entry):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = dir_path + "/txts/log.html"

        ip = requests.get('http://ip.42.pl/raw').text

        with open(file_path, "a+") as log:
            if os.path.getsize(file_path) > 0:
                log.write("\nFunction:" + entry +
                "\n\tTimestamp: " + str(datetime.now()) + 
                "\n\tExectued from: " + ip +
                "\n")
            else:        
                log.write("Function:" + entry +     
                "\n\tTimestamp: " + str(datetime.now()) + 
                "\n\tExectued from: " + ip +
                "\n")


    def getPersonalData(self):
        print('[+] Fetching Data')
        api.getSelfUserFollowers()
        result = api.LastJson
        for user in result['users']:
            self.follower_users.append({'pk': user['pk'], 'username': user['username']})
        api.getSelfUsersFollowing()
        result = api.LastJson
        for user in result['users']:
            self.following_users.append({'pk': user['pk'], 'username': user['username']})
        
        self.writeLog("getPersonalData of " + user["username"])

        return self.follower_users, self.following_users


    def getUsers(self, account):
        api.searchUsername(account)
        result = api.LastJson
        username_id = result['user']['pk']
        api.getUserFeed(username_id)
        result = api.LastJson
        media_id = result['items'][0]['id']
        api.getMediaLikers(media_id)
        users = api.LastJson['users']
        for user in users:
            self.users_list.append({'pk': user['pk'], 'username': user['username']})
        print('[+] '+ str(len(self.users_list)) +' Users fetched')
        return self.users_list


    def getPicsAccount(self, account):
        print('[+] Fetching Pics from Account')
        path = os.path.join(self.programpath, 'pictures/')
        if not os.path.exists(path):
            os.makedirs(path)
        api.searchUsername(account)
        result = api.LastJson
        username_id = result['user']['pk']
        api.getUserFeed(username_id)
        result = api.LastJson
        for i in range(len(result)):
            if result['items'][i]['media_type'] == 1:
                url = result['items'][i]['image_versions2']['candidates'][0]['url']
                print(url)
                openurl = urllib.request.urlopen(url)
                f = open(path + str(i), 'wb')
                f.write(openurl.read())
                f.close()
                if os.path.getsize(path + str(i)) < 1000:
                    os.remove(path + str(i))


    def getPicsHashtag(self, hashtag):
        print('Get pictures')
        path = self.programpath + '/pictures'
        if not os.path.exists(path):
            os.makedirs(path)
        api.getHashtagFeed(hashtag)
        result = api.LastJson
        for i in range(len(result)):
            if result['items'][i]['media_type'] == 1:
                url = result['items'][i]['image_versions2']['candidates'][0]['url']
                print(url)
                openurl = urllib.request.urlopen(url)
                f = open(path + '/' + str(i) + '.jpg', 'wb')
                f.write(openurl.read())
                f.close()
                if os.path.getsize(path + '/' + str(i) + '.jpg') < 1000:
                    os.remove(path + '/' + str(i) + '.jpg')


    def followUsers(self, max):
        print('Follow ' + str(max) + ' users')
        index = 0
        for user in self.users_list:
            if not user['pk'] in self.following_users:
                index += 1
                api.follow(user['pk'])
                if api.LastJson['status'] == 'fail':
                    print('Failed to follow @' + user['username'])
                else:
                    if api.LastJson['friendship_status']['following'] == 'True':
                        print('Now following @' + user['username'])
                        api.getUserFeed(user['pk'])
                        api.like(api.LastJson['items'][0]['id'])
                    else:
                        print('Trying to follow @' + user['username'])
                waittime = randint(30, 60)
                print('Waiting ' + str(waittime) + ' seconds')
                sleep(waittime)
            else:
                print('Already following @' + user['username'])
            if index == max:
                print('Tried to follow ' + str(index) + ' people')
                return


    def followUser(self, user):
        pk = user['pk']
        username = user['username']
        api.follow(pk)
        result = api.LastJson
        print(result)
        if result['status'] == 'fail':
            print('Failed to follow @' + username)
        else:
            if result['friendship_status']['following'] == 'True':
                print('Now following @' + username)
                api.getUserFeed(pk)
                result = api.LastJson
                if len(result['items']) > 0:
                    api.like(result['items'][0]['id'])
            else:
                print('Trying to follow @' + username)


    def unfollowUser(self, user):
        api.unfollow(user['pk'])
        if api.LastJson['status'] == 'ok':
            print('Unfollowed @' + user['username'])
        else:
            print('Failed to unfollow @' + user['username'])


    def unfollowAll(self):
        for user in self.following_users:
            print('Unfollow all users')
            print('Unfollowing @' + user['username'])
            api.unfollow(user['pk'])
            # set this really long to avoid from suspension
            sleep(randint(300, 600))

    def randomHashtag(self, amount):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + "/txts/hashtags.txt") as f:
            hashtagList = f.read().splitlines()
        hashtagString = ""
        hashtags = []
        while len(hashtags) < amount:
            tag = choice(hashtagList) 
            if not tag in str(hashtags):
                hashtags.append(tag)
                hashtagString = hashtagString + " " + tag
        return hashtagString

    def generateTempFile(self, photo_path, caption):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + "/txts/temp.txt", "rw") as f:
            f.write(photo_path)
            f.write(caption)
    
    def postPicture(self, caption, picname, username, password):
        #post pic code snippet 
        #todo caption can only be one word long because otherwise it overrides username and password
        dir_path = os.path.dirname(os.path.realpath(__file__))
        caption = caption + "\n" + self.randomHashtag(9)
        command = "node ./postpics.js "  + username[:-1] + " " + password + " " + picname + " " + "'" + caption + "'" 
        os.chdir(dir_path + '/js')
        os.system(command)
        os.chdir(dir_path)

