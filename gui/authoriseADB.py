import command
from subprocess import run, PIPE
from tkinter import *

root = Tk()
root.title("Authorise ADB")

canvas1 = Canvas(root, width=350, height=150)
canvas1.pack(padx=1, pady=1)

entry1 = Entry(root)
canvas1.create_window(90, 15, window=entry1)

def sdk_checker():
    adb_fastboot = entry1.get()
    if adb_fastboot.lower() == "adb":
        sdk_check = run([command.adb, "devices"], stdout=PIPE, stderr=PIPE, text=True)
        label1 = Label(root, text=sdk_check.stdout) 
        canvas1.create_window(90, 60, window=label1)
    elif adb_fastboot.lower() == "fastboot":
        sdk_check = run([command.fastboot, "devices"], stdout=PIPE, stderr=PIPE, text=True)
        label1 = Label(root, text=sdk_check.stdout)
        canvas1.create_window(90, 60, window=label1)
    else:
        test = "ERROR: Please type adb or fastboot in the input field."
        label1 = Label(root, text=test)
        canvas1.create_window(150, 60, window=label1)

btn1 = Button(text="Check", command=sdk_checker)
canvas1.create_window(200, 15, window=btn1)

btn2 = Button(text="Back", command=exit)
canvas1.create_window(260, 15, window=btn2)

root.mainloop()