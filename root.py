from subprocess import run, PIPE
import command

def root():
    print("Which option would you like?")
    print("1. Root wtih MM Root\t\t\t\t", "2. Root with LP Root")
    ins = int(input(": "))

    def con(value, name):
        if value.returncode == 0:
            print(value.stdout)
            print(f"Launch TWRP and flashh {name}. Which should be available on your sdcard")
        else:
            print(value.stderr)

    if ins == 1:
        print("Rooting with MM Root file....")
        root = run((command.adb, "push", "mm-root.zip", "/sdcard/"), stdout=PIPE, stderr=PIPE, text=True)
        mm = "MM-root.zip"
        con(root, mm)
    elif ins == 2:
        print("Rooting with LP Root file....")
        root = run((command.adb, "push", "lp-root.zip", "/sdcard/"), stdout=PIPE, stderr=PIPE, text=True)
        lp = "lp-root.zip"
        con(root, lp)

        reboot = run((command.adb, "reboot-bootloader"), stdout=PIPE, stderr=PIPE, text=True)
        r = None
        con(reboot, r) 

    else:
        exit()