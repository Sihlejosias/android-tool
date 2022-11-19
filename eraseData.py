###
# This small programe erase or format the userdata partition
#
##

import platform, subprocess

def eraseData():
    from Droidk import start
    command = "fastboot.exe" if platform.system() == "Windows" else "fastboot"
    erase = subprocess.run((command, "erase", "userdata"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if erase.returncode == 0:
        print(erase.stdout)
        start()
    else:
        print(erase.stderr)
        oem_unlock = subprocess.run((command, "oem", "unlock"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if oem_unlock.returncode == 0:
            print(oem_unlock.stdout)
        else:
            print(oem_unlock.stderr)
            Type = input("Type: system or recovery or userdata: ")
            Format = subprocess.run((command, "format", Type), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if Format == 0:
                print(Format.stdout)
            else:
                print(Format.stderr)
        start()