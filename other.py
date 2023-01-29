import subprocess
import os 

# god this code sucks, i should find a way to make it so I don't need to do an if/else statement for every command...

def open():
    if os.path.exists("./palera1n"):
        os.chdir("./palera1n")
        subprocess.call(["git", "pull"])
    else:
        subprocess.call(["git", "clone", "--recursive", "https://github.com/palera1n/palera1n"])

def dfuhelper():
    if os.path.exists("./palera1n"):
        os.chdir("./palera1n")
        subprocess.call(["sudo", "./palera1n.sh", "--dfuhelper"])
    else:
        print("[!] palera1n not installed, press Clone/Pull in the GUI")

def uninstall():
    if os.path.exists("./palera1n"):
        print("[*] Uninstalling palera1n...")
        subprocess.call(["sudo", "rm", "-rf", "./palera1n"])
        print("[*] palera1n has been successfully uninstalled!")
    else:
        print("[!] Can't uninstall palera1n because it isn't installed in the first place...")