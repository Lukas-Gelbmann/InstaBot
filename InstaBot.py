import InstaModule
import os
from random import choice, randint
from time import sleep
import datetime
import sys
import datetime

def main():
    # passing command line arguments w/ credentials
    username = sys.argv[1]
    password = sys.argv[2]

    print("\nLaunching bot with credentials:")
    print("\tUsername: " + username)
    print("\tPassword: " + password)
    print("\tStarting time: " + str(datetime.datetime.now()))
    print("\n\n")

    #login
    bot = InstaModule.InstaBotFunctions(username,password)
    followedusers = []
    picnumber = 0

    #start
    while True:
        #timer to start
        start = '14:00:00'
        startend = '14:01:00'
        print('waiting until ' + start)
        while start > str(datetime.datetime.today().time()) or startend < str(datetime.datetime.today().time()):
            sleep(10)

        #here you are at 10am
        print('start')
        sleep(randint(10,30))

        #getting users to follow
        print('fetching data')
        bot.getPicsHashtag()
        sleep(randint(10,30))
        follower, following = bot.getPersonalData()
        fetchedusers = bot.getUsers("doggosdoingthings")
        goodusers = []
        for user in fetchedusers:
            if not user in follower or following:
                goodusers.append(user)
        sleep(randint(10,30))
        #postpicture
        print('post pictures')
        for _ in range(3):
            picnumber = picnumber + 1
            bot.postPicture('We love dogs!', str(picnumber) + '.jpeg', username, password)
            sleep(randint(3000,4000))

        #follow / unfollow
        print('follow / unfollow')
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

    
main()