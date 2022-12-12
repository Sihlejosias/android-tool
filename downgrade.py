from subprocess import run, PIPE
import command

def downgrading():
    print("Please make sure that the Lollipop firmware is in the same directory or folder as to Droidk.py file.\n")
    confrim = input("Confirm: Are you sure you want to downgrade to android Lollipop? (Yes or No): ")
    if confrim.lower() == "yes" or confrim.lower() == "y":
        bootloader = run((command.adb, "reboot-bootloader"), stdout=PIPE, stderr=PIPE)
        bootloader_q = input("Is device in bootloader Mode?")

        if bootloader.returncode == 0 and bootloader_q == "yes":
            run(("@echo", "off"))
            
            def contitional(value):
                if value.returncode == 0:
                    print(value.stdout)
                else:
                    print(value.stderr)

            print("Partition table has been SKIPPED", "\nBootloader have been SKIPPED")

            print("Flashing Boot Logo")
            logo_flash = run((command.fastboot, "flash", "logo", "logo.bin"), stdout=PIPE, stderr=PIPE)
            contitional(logo_flash)

            print("Flashing boot image....")
            boot_flash = run((command.fastboot, "flash", "boot", "boot.img"), stdout=PIPE, stderr=PIPE)
            contitional(boot_flash)

            print("Flasshing Recovery image....")
            recovery_flash = run((command.fastboot, "flash", "recovery", "recovery.img"), stdout=PIPE, stderr=PIPE)
            contitional(recovery_flash)
            
            print("FLashing system partitions....")
            for i in range(7):
                system_flash = run((command.fastboot, "flash", "system", f"system.img_sparsechunk.{i}"), stdout=PIPE, stderr=PIPE)
                contitional(system_flash)
            print("System partitions successfully flashed")

            print("Flashing modem....")
            modem_flash = run((command.fastboot, "flash", "modem", "NON-HLOS.bin"), stdout=PIPE, stderr=PIPE)
            contitional(modem_flash)
            print("Erasing old data....")
            for i in range(1,3):
                md_erase = run((command.fastboot, "erase", f"modemst{i}"), stdout=PIPE, stderr=PIPE)
                contitional(md_erase)
            
            print("Flashing FSG....")
            fsg_flash = run((command.fastboot, "flash", "fsg", "fsg.mbn"), stdout=PIPE, stderr=PIPE)
            contitional(fsg_flash)

            print("Erasing cache and userdata")
            cache_erase = run((command.fastboot, "erase", "cache"), stdout=PIPE, stderr=PIPE)
            contitional(cache_erase)
            userdata_erase = run((command.fastboot, "erase", "userdata"), stdout=PIPE, stderr=PIPE)
            contitional(userdata_erase)

            print("Finishing the downgrade....")
            reboot = run((command.fastboot, "reboot"), stdout=PIPE, stderr=PIPE)
            contitional(reboot)

            print("Enjoy Lollipop again!")

        else:
            print(bootloader.stderr)
    else:
        print("Choose the correct option next time.")
