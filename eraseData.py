import platform, subprocess

def eraseData():
    command = "fastboot.exe" if platform.system() == "Windows" else "fastboot"
    erase = subprocess.run((command, "erase", "userdata"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if erase.returncode == 0:
        print(erase.stdout)
    else:
        print(erase.stderr)
        oem_unlock = subprocess.run((command, "oem", "unlock"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if oem_unlock.returncode == 0:
            print(oem_unlock.stdout)
        else:
            print(oem_unlock.stderr)