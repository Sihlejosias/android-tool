from tkinter import *
import command
from subprocess import run, PIPE

root = Tk()
root.geometry("450x350")
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
        label2.pack(pady=9)

        canvas1 = Canvas(root, width=350, height=350)
        canvas1.pack(padx=10, pady=20)

        erase = run((command.fastboot, "erase", "userdata"), stdout=PIPE, stderr=PIPE, text=True)
        if erase.returncode == 0:
            success = Label(root, text=erase.stdout)
            canvas1.create_window(80, 15, window=success)
        else:
            fail = Label(root, text=erase.stderr)
            canvas1.create_window(80, 15, window=fail)
            oem_unlock = run((command.fastboot, "oem", "unlock"), stdout=PIPE, stderr=PIPE, text=True)
            if oem_unlock.returncode == 0:
                success = Label(root, text=oem_unlock.stdout)
                canvas1.create_window(120, 50, window=success)
            else:
                fail = Label(root, text=oem_unlock.stderr)
                canvas1.create_window(120, 50, window=fail) 
                Format = run((command.fastboot, "format", "userdata"), stdout=PIPE, stderr=PIPE, text=True)
                if Format.returncode == 0:
                    success = Label(root, text=Format.stdout)
                    canvas1.create_window(120, 100, window=success)
                else:
                    fail = Label(root, text=Format.stderr)
                    canvas1.create_window(120, 100, window=fail)

    btn2 = Button(text="Erase Userdate", command=eraseData)
    btn2.pack()

    def customRecovery():
        delt()

        label2 = Label(root, text="Custom Recovery")
        label2.pack(pady=10)

        label3 = Label(root, text="Installing TWRP. Please choose the version you want to install.")
        label3.pack(pady=1)

        canvas1 = Canvas(root, width=450, height=350)
        canvas1.pack(padx=10, pady=10)
        
        def con(value):
            if value.returncode == 0:
                success = Label(root, text=value.stdout)
                canvas1.create_window(70, 120, window=success)
            else:
                fail = Label(root, text=value.stderr)
                canvas1.create_window(70, 120, window=fail)

        def twrp3R1():
            twrp = run((command.fastboot, "flash", "recovery", "twrp/TWRP3.4.5R1.img"), stdout=PIPE, stderr=PIPE, text=True)
            con(twrp)

        r1 = Button(text="Version 3.4.5 R1", command=twrp3R1)
        canvas1.create_window(70, 20, window=r1)

        def twrp2t():
            twrp = run((command.fastboot, "flash", "recovery", "twrp/TWRP2.8.7TESTING.img"), stdout=PIPE, stderr=PIPE, text=True)
            con(twrp)

        r2 = Button(text="Version 2.8.7 Testing", command=twrp2t)
        canvas1.create_window(210, 20, window=r2)

        def twrp2R2():
            twrp = run((command.fastboot, "flash", "recovery", "twrp/TWRP2.8.7R2.img"), stdout=PIPE, stderr=PIPE, text=True)
            con(twrp)

        r3 = Button(text="Version 2.8.7 R2", command=twrp2R2)
        canvas1.create_window(350, 20, window=r3)

        def twrp2R3():
            twrp = run((command.fastboot, "flash", "recovery", "twrp/TWRP2.8.7R3.img"), stdout=PIPE, stderr=PIPE, text=True)
            con(twrp)

        r4 = Button(text="Version 2.8.7 R3", command=twrp2R3)
        canvas1.create_window(70, 50, window=r4)

        def twrp2R4():
            twrp = run((command.fastboot, "flash", "recovery", "twrp/TWRP2.8.7R4.img"), stdout=PIPE, stderr=PIPE, text=True)
            con(twrp)

        r5 = Button(text="Version 2.8.7 R4", command=twrp2R4)
        canvas1.create_window(198, 50, window=r5)

        def twrp2R5():
            twrp = run((command.fastboot, "flash", "recovery", "twrp/TWRP2.8.7R5.img"), stdout=PIPE, stderr=PIPE, text=True)
            con(twrp)

        r6 = Button(text="Version 2.8.7 R5", command=twrp2R5)
        canvas1.create_window(324, 50, window=r6)

        def twrp2R7():
            twrp = run((command.fastboot, "flash", "recovery", "twrp/TWRP2.8.7R7.img"), stdout=PIPE, stderr=PIPE, text=True)
            con(twrp)

        r7 = Button(text="Version 2.8.7 R7", command=twrp2R7)
        canvas1.create_window(70, 80, window=r7)

    btn3 = Button(text="Custom Recovery", command=customRecovery)
    btn3.pack()
    
    def downgrade():
        delt()

        label2 = Label(root, text="Downgrade To Lollipo")
        label2.pack(pady=10)

        canvas1 = Canvas(root, width=450, height=350, background="black")
        canvas1.pack(pady=10, padx=10)

        label4 = Label(root, text=">> ", background="black", fg="white")
        canvas1.create_window(15, 15, window=label4)
        label3 = Label(root, text="Starting! Please don't switch off the devices or it may brick you phone.", fg="white", background="black")
        canvas1.create_window(220, 16, window=label3)
        label5 = Label(root, text=">>", background="black", fg="white")
        canvas1.create_window(15, 35, window=label5)


    btn4 = Button(text="Downgrade to Lollipop", command=downgrade)
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