import InstaModule
import os
from random import choice, randint
from time import sleep
import datetime

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/txts/credentials.txt", "r") as credentialFile:
        username = credentialFile.readline()
        password = credentialFile.readline()

    #login
    bot = InstaModule.InstaBotFunctions(username,password)
    followedusers = []


    #start
    while True:
        #timer to start
        start = '16:00:00'
        startend = '16:01:00'
        print('waiting until ' + start)
        while start > str(datetime.datetime.today().time()) or startend < str(datetime.datetime.today().time()):
            sleep(10)
        #here you are at 10am
        print('start')
        sleep(randint(0,600))


        #getting users to follow
        print('fetching data')
        follower, following = bot.getPersonalData()
        fetchedusers = bot.getUsers("doggosdoingthings")
        goodusers = []
        for user in fetchedusers:
            if not user in follower or following:
                goodusers.append(user)

        print('doing stuff')
        for _ in range(12):
            #follow
            sleep(randint(300,600))
            followuser = choice(goodusers)
            followedusers.append(followuser)
            bot.followUser(followuser)
            goodusers.remove(followuser)
            sleep(randint(300,600))
            if len(followedusers) > 24:
                #unfollow
                bot.unfollowUser(followedusers[0])
                followedusers.remove(followedusers[0])
            sleep(randint(3000,4000))

        #postpicture
        bot.postPicture('We love dogs!', '125.jpeg', username, password)

main()