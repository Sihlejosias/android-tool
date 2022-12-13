###
# This small programe erase or format the userdata partition
#
##

from subprocess import run, PIPE
import command

def eraseData():
    from Droidk import start
    erase = run((command.fastboot, "erase", "userdata"), stdout=PIPE, stderr=PIPE, text=True)
    if erase.returncode == 0:
        print(erase.stdout)
        start()
    else:
        print(erase.stderr)
        oem_unlock = run((command.fastboot, "oem", "unlock"), stdout=PIPE, stderr=PIPE, text=True)
        if oem_unlock.returncode == 0:
            print(oem_unlock.stdout)
        else:
            print(oem_unlock.stderr)
            Type = input("Type: system or recovery or userdata: ")
            format = run((command.fastboot, "format", Type), stdout=PIPE, stderr=PIPE, text=True)
            command.con(format)
        start()