import subprocess, platform

def downgrading():
    print("Please make sure that the Lollipop firmware is in the same directory or folder as to Droidk.py file.\n")
    confrim = input("Are you sure you want to downgrade to android Lollipop? ")
    if confrim == "yes" or confrim == "YES" or confrim == "Yes" or confrim == "y" or confrim == "Y":
        command = "adb.exe" if platform.system() == "Windows" else "adb"
        bootloader = subprocess.run((command, "reboot-bootloader"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        confrim2 = input("Is device in bootloader Mode?")

        if bootloader.returncode == 0 and confrim2 == "yes":
            command2 = "fastboot.exe" if platform.system() == "Windows" else "fastboot"
            subprocess.run(("@echo", "off"))

            print("Partition table has been SKIPPED", "\nBootloader have been SKIPPED")
            logo_flash = subprocess.run((command2, "flash", "logo", "logo.bin"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if logo_flash.returncode == 0:
                print(logo_flash.stdout)
            else:
                print(logo_flash.stderr)
        else:
            print(bootloader.stderr)
    else:
        print("Choose the correct option next time.")

downgrading()