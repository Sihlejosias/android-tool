from platform import system

adb = "adb.exe" if system() == "Windows" else "adb"
fastboot = "fastboot.exe" if system() == "Windows" else "fastboot"
locator = "where" if system() == "Windows" else "which"

def con(value):
    if value.returncode == 0:
        print(value.stdout, end="")
    else:
        print(value.stderr, end="")
#Add Download command