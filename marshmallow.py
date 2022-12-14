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
            table_flash = run((command.fastboot, "flash", "partition", "gpt.bin"), stdout=PIPE, stderr=PIPE, text=True)
            command.con(table_flash)

            print("Flashing bootloader....")
            bootf = run((command.fastboot, "flash", "bootloader", "bootloader.img"), stdout=PIPE, stderr=PIPE, text=True)
            command.con(bootf)

            print("Flashing boot logo....")
            logo_flash = run((command.fastboot, "flash", "logo", "logo.bin"), stdout=PIPE, stderr=PIPE, text=True)
            command.con(logo_flash)

            print("Flashing boot image....")
            boot_flash = run((command.fastboot, "flash", "boot", "boot.img"), stdout=PIPE, stderr=PIPE, text=True)
            command.con(boot_flash)

            print("Flashing recovery image...")
            recovery = run((command.fastboot, "flash", "recovery", "recovery.img"), stdout=PIPE, stderr=PIPE, text=True)
            command.con(recovery)

            print("Flashing system image....")
            for i in range(7):
                system_flash = run((command.fastboot, "flash", "system", f"system.img_sparsechunk.{i}"))
                command.con(system_flash)
            print("System partition successfully flashed. ")

            print("Flashing Modem...")
            md_flash = run((command.fastboot, "flash", "modem", "NON-HLOS.bin"), stdout=PIPE, stderr=PIPE, text=True)
            command.con(md_flash)

            print("Erasing old data...")
            for i in range(1, 3):
                erase_flash = run((command.fastboot, "erase", f"modemst{i}"), stdout=PIPE, stderr=PIPE, text=True)
                command.con(erase_flash)
            print("Old data erased")

            print("Flashing FSG....")
            fsg_flash = run((command.fastboot, "flash", "fsg", "fsg.mbn"), stdout=PIPE, stderr=PIPE, text=True)
            command.con(fsg_flash)

            print("Erasing cache and userdate....")
            cache_erase = run((command.fastboot, "erase", "cache"), stdout=PIPE, stderr=PIPE,text=True)
            command.con(cache_erase)
            reboot = run((command.fastboot, "reboot"), stdout=PIPE, stderr=PIPE, text=True)
            command.run(reboot)

            print("Enjoy Marshmallow. :-)")
            
        else:
            print("Device not in bootloader")
    else:  
        print("Choose an approprite solution.")