import InstagramAPI
from random import randint, seed
from time import sleep
import os
import urllib.request

username = ""
password = ""
users_list = []
following_users = []
follower_users = []
postpath = '6'
programpath = os.path.dirname(__file__)

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + "/credentials.txt", "r") as credentialFile:
    username = credentialFile.readline()
    password = credentialFile.readline()

def main():
    seed(1)
    api = InstagramAPI.InstagramAPI(username, password)
    api.login()
    getdata(api)
    unfollow_all(api)
    #getusers(api, 'doggosdoingthings')
    #followusers(api, 20)
    #getpicsaccount(api, 'dogsofinstagram')
    #getpicshashtag(api, 'dogsofinstagram')
    #postpic(api, postpath)


def getdata(api):
    print('Get data')
    api.getSelfUserFollowers()
    result = api.LastJson
    for user in result['users']:
        follower_users.append({'pk': user['pk'], 'username': user['username']})
    api.getSelfUsersFollowing()
    result = api.LastJson
    for user in result['users']:
        following_users.append({'pk': user['pk'], 'username': user['username']})


def getusers(api, account):
    print('Get users')
    api.searchUsername(account)
    result = api.LastJson
    username_id = result['user']['pk']
    api.getUserFeed(username_id)
    result = api.LastJson
    media_id = result['items'][0]['id']
    api.getMediaLikers(media_id)
    users = api.LastJson['users']
    for user in users:
        users_list.append({'pk': user['pk'], 'username': user['username']})


def getpicsaccount(api, account):
    print('Get pictures')
    path = os.path.join(programpath, 'pics/')
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


def getpicshashtag(api, hashtag):
    print('Get pictures')
    path = programpath + '/pics'
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


def followusers(api, max):
    print('Follow ' + str(max) + ' users')
    index = 0
    for user in users_list:
        if not user['pk'] in following_users:
            index += 1
            print('Following @' + user['username'])
            api.follow(user['pk'])
            api.getUserFeed(user['pk'])
            result = api.LastJson
            if result['status'] == 'ok':
                print('Liking newest post')
                api.like(result['items'][0]['id'])
            waittime = randint(30, 60)
            print('Waiting ' + str(waittime) + ' seconds')
            sleep(waittime)
        else:
            print('Already following @' + user['username'])
        if index == max:
            print('Tried to follow ' + str(index) + ' people')
            return


def unfollow_all(api):
    print('Unfollow all users')
    for user in following_users:
        print('Unfollowing @' + user['username'])
        api.unfollow(user['pk'])
        # set this really long to avoid from suspension
        sleep(randint(300, 600))


def postpic(api, string): # photo = directory
    print('Post picture')
    path = programpath + '/pics/' + string + '.jpg'
    api.uploadPhoto(photo=path, caption='dog pic of the day')


main()