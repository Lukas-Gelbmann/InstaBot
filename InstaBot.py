import instaModule

def main():
    api = instaModule.InstaBotFunctions()

    api.getUsers("hypebeast")
    api.followUsers(20)



main()