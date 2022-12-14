import  command
from subprocess import run, PIPE
import time

def load():
    print("This allows you to install apk file while in bootloader sideload mode!")
    ask = input("Confirm: is device usb debugging on? (Yes or No): ")
    if ask.lower() == "y" or ask.lower() == "yes":
        auth = run((command.adb, "devices"), stdout=PIPE, stderr=PIPE, text=True)
        command.con(auth)
        
        act = run((command.adb, "tcpip", "5555"), stdout=PIPE, stderr=PIPE)
        if act.returncode == 0:
            print("Get the ip address of the device; include the following at the end of the ip addres :5555")
            ip = input("Type ip: ")
            print("Remove usb cable from your device and computer!")
            time.sleep(15)
            connect = run((command.adb, "connect", f"{ip}"), stderr=PIPE, text=True)
            command.con(connect)

            if connect.returncode == 0:
                filename = input("File name yo want to install via sideload: (e.g app.apk) ")
                install = run((command.adb, "install", f"{filename}"), stdout=PIPE, stderr=PIPE, text=True)
                print(f"{filename} is sideloading now!")
                if install.returncode == 0:
                    print(install.stdout)
                    print(f"{filename} is installed.")
                else:
                    print(install.stderr)
            else:
                print(connect.stderr)
        else:
            print(act.stderr)
        
    else:
        print("Switch on USB debugging first!")