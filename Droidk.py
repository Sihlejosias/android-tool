from authoriseADB import sdk_checker
from eraseData import eraseData

print("Welcome to Droid KIT. Let use help you today. Choose option below.")
print()
print("1. Authorise ADB")
print("2. Erase userdata")
print("3. Flash Custom Recovery")
print("4. Downgrade To Lollipop")
print("5. Reinstall Lollipop")
print("6. Flash Marshmallow")
print("7. Install Motorola USB Driver")
print("8. Wireless APK Sideload(BETA no root)")
print("9. Root")
print()

Input = int(input("Enter option(e.g 1 for Authorising ADB): "))

if Input == chr:
    print("Please use numbers")
else:
    if Input == 1: 
        sdk_checker()
    elif Input == 2:
        eraseData()
    elif Input == 3:
        print("Option currently not implimented")
    elif Input == 4:
        print("Option currently not implimented")
    elif Input == 5:
        print("Option currently not implimented")
    elif Input == 6:
        print("Option currently not implimented")
    elif Input == 7:
        print("Option currently not implimented")
    elif Input == 8:
        print("Option currently not implimented")
    elif Input == 9:
        print("Option currently not implimented")
    else: 
        print("Invalid option!")