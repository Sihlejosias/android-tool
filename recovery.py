###
# This small programe install custom recovery app to the device.
###

from subprocess import run, Popen, PIPE
import command

def recover():
    print("1. TWRP 3.4.5 R1\t\t", "2. TWRP 2.8.7 Testing Edition")
    print("3. TWRP 2.8.7 R2\t\t", "4. TWRP 2.8.7 R3")
    print("5. TWRP 2.8.7 R4\t\t", "6. TWRP 2.8.7 R5")
    print("7. TWRP 2.8.7 R7")

    version = int(input("Choose what version of TWRP for the following(e.g 1 for TWRP 3.4.5): "))

    if version == 1:
        #Near future have the ability to download and install the custom recovery option and check if available on current directory
        twrp3R1 = Popen((command.fastboot, "flash", "recovery", "twrp/TWRP3.4.5R1.img"), stdout=PIPE, stderr=PIPE).communicate()
        print("Waiting: ")
        twrp3R1.wait()
        command.con(twrp3R1)
    elif version == 2:
        twrp2T = Popen((command.fastboot, "flash", "recovery", "twrp/TWRP2.8.7TESTING.img"), stdout=PIPE, stderr=PIPE).communicate()
        print("Waiting: ")
        twrp2T.wait()
        command.con(twrp2T)
    elif version == 3:
        twrp2R2 = Popen((command.fastboot, "flash", "recovery", "twrp/TWRP2.8.7R2.img"), stdout=PIPE, stderr=PIPE).communicate()
        print("Waiting: ")
        twrp2R2.wait()
        command.con(twrp2R2)
    elif version == 4:
        twrp2R3 = Popen((command.fastboot, "flash", "recovery", "twrp/TWRP2.8.7R3.img"), stdout=PIPE, stderr=PIPE).communicate()
        print("Waiting: ")
        twrp2R3.wait()
        command.con(twrp2R3)
    elif version == 5:
        twrp2R4 = Popen((command.fastboot, "flash","recovery","twrp/TWRP2.8.7R4.img"), stdout=PIPE, stderr=PIPE).communicate()
        print("Waiting")
        twrp2R4.wait()
        command.con(twrp2R4)
    elif version == 6:
        twrp2R5 = Popen((command.fastboot, "flash", "recovery", "twrp/TWRP2.8.7R5.img"), stdout=PIPE, stderr=PIPE).communicate()
        print("Waiting: ")
        twrp2R5.wait()
        command.con(twrp2R5)
    elif version == 7:
        twrp2R7 = Popen((command.fastboot, "flash", "recovery", "twrp/TWRP2.8.7R7.img"), stdout=PIPE, stderr=PIPE).communicate()
        print("Waiting: ")
        twrp2R7.wait()
        command.con(twrp2R7)
    else: 
        print("Invalid option") 

