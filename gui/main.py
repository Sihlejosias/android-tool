from tkinter import *
import command
from subprocess import run, PIPE

root = Tk()
root.geometry("350x350")
root.title("Android Tools")

def menu():
    def delt():
        label1.destroy()
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        btn5.destroy()
        btn6.destroy()
        btn7.destroy()
        btn8.destroy()

    label1 = Label(root, text="Menu")
    label1.pack(pady=9)

    def authoriseADB():
        delt()
        label2 = Label(root, text="ADB and FASTBOOT device check")
        label2.pack(pady=9)

        canvas1 = Canvas(root, width=350, height=350)
        canvas1.pack(padx=10, pady=10)

        entry1 = Entry(root)
        canvas1.create_window(80, 15, window=entry1)
        
        def sdk_checker():
            adb_fastboot = entry1.get()
            if adb_fastboot.lower() == "adb":
                adb = run((command.adb, "devices"), stdout=PIPE, stderr=PIPE, text=True)
                if adb.returncode == 0:
                    success = Label(root, text=adb.stdout)
                    canvas1.create_window(150, 60, window=success) 
                else:
                    fail = Label(root, text=adb.stderr)
                    canvas1.create_window(150, 60, window=fail)
            elif adb_fastboot.lower() == "fastboot":
                fastboot = run((command.fastboot, "devices"), stdout=PIPE, stderr=PIPE, text=True)
                if fastboot.returncode == 0:
                    success = Label(root, text=fastboot.stdout)
                    canvas1.create_window(150, 60, window=success) 
                else:
                    fail = Label(root, text=fastboot.stderr)
                    canvas1.create_window(150, 60, window=fail)
            else:
                err = "Error: invalid input. Please type adb or fastboot."
                errbox = Label(root, text=err)
                canvas1.create_window(150, 60, window=errbox)
        
        check = Button(text="Check", command=sdk_checker)
        canvas1.create_window(190, 15, window=check)
        def bc():
            label2.destroy()
            canvas1.destroy()
            menu()
        back = Button(text="Back", command=bc)
        canvas1.create_window(250, 15, window=back)

    btn1 = Button(text="authorise ADB", command=authoriseADB)
    btn1.pack()

    def eraseData():
        delt()
        
        label2 = Label(root, text="Erase userdata")
        label2.pack()

    btn2 = Button(text="Erase Userdate", command=eraseData)
    btn2.pack()

    btn3 = Button(text="Custom Recovery", command=exit)
    btn3.pack()

    btn4 = Button(text="Downgrade to Lollipop", command=exit)
    btn4.pack()

    btn5 = Button(text="Flash Lollipop", command=exit)
    btn5.pack()

    btn6 = Button(text="Flash Marshmallow", command=exit)
    btn6.pack()

    btn7 = Button(text="Wireless APK Sideload", command=exit)
    btn7.pack()

    btn8 = Button(text="root", command=exit)
    btn8.pack()

menu()
root.mainloop()