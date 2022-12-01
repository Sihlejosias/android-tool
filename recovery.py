###
# This small programe install custom recovery app to the device.
###

import platform, subprocess

def recover():
    print("1. TWRP 3.4.5 R1\t\t", "2. TWRP 2.8.7 Testing Edition")
    print("3. TWRP 2.8.7 R2\t\t", "4. TWRP 2.8.7 R3")
    print("5. TWRP 2.8.7 R4\t\t", "6. TWRP 2.8.7 R5")
    print("7. TWRP 2.8.7 R7")

    version = int(input("Choose what version of TWRP for the following(e.g 1 for TWRP 3.4.5): "))
    command = "fastboot.exe" if platform.system() == "Windows" else "fastboot"

    def if_else(value):
        if value.returncode == 0:
            print(value.stdout)
            print("All Done :-)")
            subprocess.run((command, "reboot"))
        else: 
            print(value.stderr)
            print("Failed!! :-(")
            subprocess.run((command, "reboot"))

    if version == 1:
        #Near future have the ability to download and install the custom recovery option and check if available on current directory
        twrp3R1 = subprocess.Popen((command, "flash", "recovery", "twrp/TWRP3.4.5R1.img"), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        print("Waiting: ")
        twrp3R1.wait()
        if_else(twrp3R1)
    elif version == 2:
        twrp2T = subprocess.Popen((command, "flash", "recovery", "twrp/TWRP2.8.7TESTING.img"), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        print("Waiting: ")
        twrp2T.wait()
        if_else(twrp2T)
    elif version == 3:
        twrp2R2 = subprocess.Popen((command, "flash", "recovery", "twrp/TWRP2.8.7R2.img"), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        print("Waiting: ")
        twrp2R2.wait()
        if_else(twrp2R2)
    elif version == 4:
        twrp2R3 = subprocess.Popen((command, "flash", "recovery", "twrp/TWRP2.8.7R3.img"), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        print("Waiting: ")
        twrp2R3.wait()
        if_else(twrp2R3)
    elif version == 5:
        twrp2R4 = subprocess.Popen((command, "flash","recovery","twrp/TWRP2.8.7R4.img"), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        print("Waiting")
        twrp2R4.wait()
        if_else(twrp2R4)
    elif version == 6:
        twrp2R5 = subprocess.Popen((command, "flash", "recovery", "twrp/TWRP2.8.7R5.img"), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        print("Waiting: ")
        twrp2R5.wait()
        if_else(twrp2R5)
    elif version == 7:
        twrp2R7 = subprocess.Popen((command, "flash", "recovery", "twrp/TWRP2.8.7R7.img"), stdout=subprocess.PIPE, stderr=subprocess.PIPI).communicate()
        print("Waiting: ")
        twrp2R7.wait()
        if_else(twrp2R7)
    else: 
        print("Invalid option") 

