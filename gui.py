from tkinter import *
import time
import subprocess
from other import *
import sys
from sys import platform

if platform == "win32":
    print("[!] palera1n does not work on Windows")
    sys.exit()
else:
    print(f'Running on {platform}')
    


root = Tk()
root.geometry("235x300")
root.title('shitty palera1n gui')

txt = Label(root, text="Shitty palera1n GUI")
txt.grid(row=1, column=0)

txt1 = Label(root, text="Press Clone/Pull to install palera1n.")
txt1.grid(row=2, column=0)
btn = Button(root, text="Clone/Pull", command = open)
btn.grid(row=3, column=0)

btn1 = Button(root, text="DFU Helper", command=dfuhelper)
btn1.grid(row=4, column=0)

versions = [
    "15.0",
    "15.0.1",
    "15.0.2",
    "15.1",
    '15.2',
    "15.2.1",
    "15.3",
    "15.3.1",
    "15.4",
    "15.4.1",
    "15.5",
    "15.6",
    "15.6.1",
    "15.7",
    "15.7.1",
    "15.7.2",
    "15.7.3",
    "16.0",
    "16.0.2",
    "16.0.3",
    "16.1",
    "16.1.1",
    "16.1.2",
    "16.2",
    "16.3",
    "16.3.1"
]

selected = StringVar(root)
selected.set(versions[0])

dropdown = OptionMenu(root, selected, *versions)
dropdown.grid(row=5, column=0)
versionselected = selected.get()

semitether = True
stcolour = "green"





def jailbreak():
    global palera1n
    if os.path.exists("./palera1n"):
        os.chdir("./palera1n")
        if semitether == True:
            palera1n = subprocess.Popen(["sudo", "./palera1n.sh", "--tweaks", versionselected, "--semi-tethered"])
        elif semitether == False:
            palera1n = subprocess.Popen(["sudo", "./palera1n.sh", "--tweaks", versionselected])
        os.chdir("..")
    else:
        print("[!] palera1n is not installed. Please run Clone/Pull.")

def restorerootfs():
    global palera1n
    if os.path.exists('./palera1n'):
        os.chdir("./palera1n")
        if semitether == True:
            palera1n = subprocess.Popen(["sudo", "./palera1n.sh", "--tweaks", versionselected, "--semi-tethered", "--restorerootfs"])
        elif semitether == False:
            palera1n = subprocess.Popen(["sudo", "./palera1n.sh", "--tweaks", versionselected, "--restorerootfs"])
        os.chdir("..")
    else:
        print("[!] palera1n not installed. Please press Clone/Pull to install it")


def semitetherbutton():
    global semitether
    global stcolour
    if semitether == True:
        semitether = False
        stcolour = "red"
    elif semitether == False:
        semitether = True
        stcolour = "green"
#h    print(semitether)
    btn2.configure(fg = stcolour)




def cancel():
    print("Killing palera1n...")
    try:
        palera1n.terminate()
    except:
        otherterminate()


btn2 = Button(root, text="Semi-Tethered", command = semitetherbutton, fg="green")
btn2.grid(row=6, column=0)

btn3 = Button(root, text="Jailbreak!", command = jailbreak)
btn3.grid (row=7, column=0)

btn4 = Button(root, text="Restore rootFS", command =restorerootfs)
btn4.grid(row=8, column=0)

btn5 = Button(root, text="Stop palera1n (unsafe)", bg="red",command=cancel)
btn5.grid(row = 9, column = 0)

btn6 = Button(root, text="Uninstall palera1n (unsafe)", bg = "red", command = uninstall)
btn6.grid(row=10, column = 0)

btn7 = Button(root, text = "Rootfull")

root.mainloop()