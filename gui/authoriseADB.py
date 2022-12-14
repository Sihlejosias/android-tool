import subprocess, platform
from tkinter import *

root = Tk()
root.title("Authorise ADB")

canvas1 = Canvas(root, width=350, height=150)
canvas1.pack(padx=1, pady=1)

entry1 = Entry(root)
canvas1.create_window(90, 15, window=entry1)

def sdk_checker():
    adb_fastboot = entry1.get()
    if adb_fastboot == "adb" or adb_fastboot == adb_fastboot:
        sdk_check = subprocess.run([adb_fastboot, "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        label1 = Label(root, text=sdk_check.stdout)
        canvas1.create_window(90, 40, window=label1)
    else:
        test = "Test"
        label2 = Label(root, text=test)
        canvas1.create_window(90, 50, window=label2)

btn = Button(text="Check", command=sdk_checker)
canvas1.create_window(160, 15, window=btn)

root.mainloop()
