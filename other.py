import subprocess
import os 
import sys
import time



# god this code sucks, i should find a way to make it so I don't need to do an if/else statement for every command...

def open():
    global palera1n
    if os.path.exists("./palera1n"):
        os.chdir("./palera1n")
        palera1n = subprocess.Popen(["git", "pull"])
        os.chdir("..")
    else:
        palera1n = subprocess.Popen(["git", "clone", "--recursive", "https://github.com/palera1n/palera1n"])

def dfuhelper():
    if os.path.exists("./palera1n"):
        os.chdir("./palera1n")
        palera1n = subprocess.Popen(["sudo", "./palera1n.sh", "--dfuhelper"])
        os.chdir('..')
    else:
        print("[!] palera1n not installed, press Clone/Pull in the GUI")

def uninstall():
    global palera1n
    if os.path.exists("./palera1n"):
        print("[*] Uninstalling palera1n...")
        subprocess.call(["sudo", "rm", "-rf", "./palera1n"])
        print("[*] palera1n has been successfully uninstalled!")
    else:
        print("[!] palera1n isn't installed")


def otherterminate():
    try:
        palera1n.terminate()
    except NameError:
        print("[!] palera1n is either not running or has already been killed.")
    except Exception as error:
        print(f"[!] An error has occured: \n {error}")