from modules.thread_handler import spool_up

#setup flow
def choice():
    print("Would you like to start a new network or join a network?")
    print("Type N, to start a new network")
    print("Type J, to join a network")
    ine = input()
    if ine.lower() == "n":
        new()
    if ine.lower() == "j":
        join()
    else:
        print("INVALID INPUT")
        choice()

def new():
    print("new network")
    spool_up(False)
def join():
    print("join network")
    spool_up(True)
