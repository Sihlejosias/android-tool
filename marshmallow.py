from subprocess import run, PIPE
import command 

def marsh():
    print("WARNNING:\n", "\tWhat you are about to do may brick your device.", "\n")
    print("Please make sure that the Lollipop firmware is in the same directory or folder as to Droidk.py file.\n")
    
    ins = input("Confirm: Do you want to install Marshmallow? (Yes or No): ")
    if ins.lower() == "yes" or ins.lower() == "y":
        bootloader_q = input("Confirm: Is device on bootloader yet? (Yes or No): ")
        bootloader_reboot = run((command.adb, "reboot-bootloader"), stdout=PIPE, stderr=PIPE)
        if bootloader_reboot.returncode == 0 and bootloader_q.lower() == "yes" or bootloader_q.lower() == "y":
            run(("@echo", "off"))

            print("Flashing partition table....")
            table_flash = run((command.fastboot, "flash", "partition", "gpt.bin"), stdout=PIPE, stderr=PIPE)
            command.con(table_flash)

            print("Flashing bootloader....")
            bootf = run((command.fastboot, "flash", "bootloader", "bootloader.img"), stdout=PIPE, stderr=PIPE)
            command.con(bootf)

            
        else:
            print("Device not in bootloader")
    else:
        print("Choose an approprite solution.")