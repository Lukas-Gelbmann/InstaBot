import InstaModule
import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/txts/credentials.txt", "r") as credentialFile:
        username = credentialFile.readline()
        password = credentialFile.readline()
    bot = InstaModule.InstaBotFunctions(username,password)
    bot.getData()
    bot.getUsers("doggosdoingthings")
    bot.followUsers(5)
    print(bot.randomHashtag(9))

main()