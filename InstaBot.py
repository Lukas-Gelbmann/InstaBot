import InstaModule
import os
from random import choice

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/txts/credentials.txt", "r") as credentialFile:
        username = credentialFile.readline()
        password = credentialFile.readline()

    #login
    bot = InstaModule.InstaBotFunctions(username,password)

    #get data
    follower, following = bot.getPersonalData()
    users = bot.getUsers("doggosdoingthings")

    #follow random user
    bot.followUser(choice(users))

    #unfollow guy which you follow
    bot.unfollowUser(choice(following))

    #post pic code snippet 
    #TODO caption can only be one word long because otherwise it overrides username and password
    caption = 'TESTcaption'
    picname = '125.jpeg'
    command = 'node ./postpics.js ' + picname + " " + caption + " " + username[:-1] + " " + password
    os.chdir(dir_path + '/js')
    os.system(command)
    os.chdir(dir_path)

    #get random hashtags
    print(bot.randomHashtag(9))

main()