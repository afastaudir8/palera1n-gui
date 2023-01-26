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


root.mainloop()