

#setup flow
def choice():
    print("Would you like to start a new network or join a network?")
    print("Type N, to start a new network")
    print("Type J, to join a network")
    ine = input()
    if ine.lower() == "n":
        pass
    if ine.lower() == "j":
        print("ok")
    else:
        print("INVALID INPUT")
        choice()
def new():
    print("new network")
def join():
    print("join network")
