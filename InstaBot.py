import instaapi
import InstagramAPI

def main():
    api = instaapi.InstaBotFunctions()

    api.getUsers("hypebeast")
    api.followUsers(20)



main()