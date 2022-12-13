from subprocess import run, PIPE
import command

def lollipop():
    print("WARNNING:\n", "\tWhat you are about to do may brick your device.", "\n")
    print("If you have a stock Marshmallow on your device, use the downgrade tool.", "\n")
    print("Please make sure that the Lollipop firmware is in the same directory or folder as to Droidk.py file.\n")

    ins = input("Confirm: Do you want to install lollipop? (Yes or No): ")
    if ins.lower() == "yes" or ins.lower() == "y":
        usb_debbug = input("Is usb debugging on you device enabled? (Yes or No): ")
        if usb_debbug.lower() == "yes" or usb_debbug.lower() == "y":
            bootloader = run((command.adb, "reboot-bootloader"), stdout=PIPE, stderr=PIPE)
            bootloader_q = input("Confirm: Has your device successfully loaded bootloader mode? (Yes or No): ")

            if bootloader.returncode == 0 and bootloader_q.lower() == "yes":
                run(("@echo", "off"))

                print("Flasshing partition table....")
                table_flash = run((command.fastboot, "flash", "partition", "gpt.bin"), stdout=PIPE, stderr=PIPE)
                command.con(table_flash)

                print("Flashing bootloader....")
                bootloader_flash = run((command.fastboot, "flash", "bootloader", "bootloader.img"), stdout=PIPE, stderr=PIPE)
                command.con(bootloader_flash)

                print("Flashing boot logo....")
                logo_flash = run((command.fastboot, "flash", "logo", "logo.bin"), stdout=PIPE, stderr=PIPE)
                command.con(logo_flash)

                print("Flashing boot image....")
                boot_flash = run((command.fastboot, "flash", "boot", "boot.img"), stdout=PIPE, stderr=PIPE)
                command.con(boot_flash)

                print("Flashing Recovery image....")
                recovery_flash = run((command.fastboot, "flash", "recovery", "recovery.img"), stdout=PIPE, stderr=PIPE)
                command.con(recovery_flash)

                print("Flashing System images....")
                for i in range(7):
                    system_flash = run((command.fastboot, "flash", "system", f"system.img_sparsechunk{i}"), stdout=PIPE, stderr=PIPE)
                    command.con(system_flash)
                print("System partitions successfully flashed.")

                print("Flasshing modem....")
                md_flash = run((command.fastboot, "flash", "modem", "NON-HLOS.bin"), stdout=PIPE, stderr=PIPE)
                command.con(md_flash)

                print("Erasing old data...")
                for i in range(1, 3):
                    erase_data = run((command.fastboot, "erase", f"modemst{i}"), stdout=PIPE, stderr=PIPE)
                    command.con(erase_data)
                print("Old data erased")

                print("Flashing FSG....")
                fsg_flash = run((command.fastboot, "flash", "fsg", "fsg.mbn"), stdout=PIPE, stderr=PIPE)
                command.con(fsg_flash)

                print("Erasing cache and userdata....")
                cache_erase = run((command.fastboot, "erase", "cache"), stdout=PIPE, stderr=PIPE)
                command.con(cache_erase)
                userdata_erase = run((command.fastboot, "erase", "userdata"), stdout=PIPE, stderr=PIPE)
                command.con(userdata_erase)

                print("Finishing to install lollipop on your device....")
                reboot = run((command.fastboot, "reboot"), stdout=PIPE, stderr=PIPE)
                command.con(reboot)

                print("You have successfully installed lollipop on your device. Enjoy!!! :-)")

            else:
                print("Could not boot to bootloader!")
        else:
            print("Please enable usb debugging before you continue....")
    else:
        print("Choose the correct option next time.")