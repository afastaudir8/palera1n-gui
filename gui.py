from tkinter import *
import time
import subprocess
from other import *

root = Tk()
root.geometry("300x300")
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
    "16.3"
]

selected = StringVar(root)
selected.set(versions[0])

dropdown = OptionMenu(root, selected, *versions)
dropdown.grid(row=5, column=0)
versionselected = selected.get()

def semitetherbutton():
    global col
    global semitether
    semitether = True
    if semitether == True:
        semitether == False
    elif semitether == False:
        semitether == True


def jailbreak():
    if os.path.exists("./palera1n"):
        os.chdir("./palera1n")
        if semitether == True:
            subprocess.call(["sudo", "./palera1n.sh", "--tweaks", versionselected, "--semi-tethered"])
        elif semitether == False:
            subprocess.call(["sudo", "./palera1n.sh", "--tweaks", versionselected])
    else:
        print("[!] palera1n is not installed. Please run Clone/Pull.")

test = 1
btn2 = Button(root, text="Semi-Tethered", command = semitetherbutton())
btn2.grid(row=6, column=0)

if semitether == True:
    btn2.configure(fg="green")
elif semitether == False:
    btn2.configure(fg="red")


root.mainloop()