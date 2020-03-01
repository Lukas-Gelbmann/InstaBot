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
    #follower, following = bot.getPersonalData()
    #users = bot.getUsers("doggosdoingthings")

    #follow random user
    #bot.followUser(choice(users))

    #unfollow guy which you follow
    #bot.unfollowUser(choice(following))

    #post pic code snippet 
    #todo caption can only be one word long because otherwise it overrides username and password
    caption = "TEST caption"
    picname = "test.jpg"
    command = "node ./postpics.js "  + username[:-1] + " " + password + " " + picname + " " + "'" + caption + "'" 
    os.chdir(dir_path + '/js')
    os.system(command)
    os.chdir(dir_path)

    #get random hashtags
    # print(bot.randomHashtag(9))

main()