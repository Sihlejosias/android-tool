from platform import system

adb = "adb.exe" if system() == "Windows" else "adb"
fastboot = "fastboot.exe" if system() == "Windows" else "fastboot"
#Add Download command