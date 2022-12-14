#!/user/bin/env python
from authoriseADB import sdk_checker
from eraseData import eraseData
from recovery import recover
from downgrade import downgrading
from lollipop import lollipop
from marshmallow import marsh
from root import root
from sideload import load 

def start():   
    print("Welcome to Droid KIT. Let use help you today. Choose option below.\n")
    print("1. Authorise ADB\t\t\t\t", "2. Erase userdata")
    print("3. Flash Custom Recovery\t\t\t", "4. Downgrade to Lollipop")
    print("5. Flash Lollipop\t\t\t\t", "6. Flash Marshmallow")
    print("7. Install Motorola USB Driver\t\t\t", "8. Wireless APK Sideload(Beta no root)")
    print("9. Root\t\t\t\t\t\t", "10. Exit\n")

    Input = int(input("Enter option(e.g 1 for Authorising ADB): "))


    if Input == 1: 
        sdk_checker()
    elif Input == 2:
        eraseData()
    elif Input == 3:
        recover()
    elif Input == 4:
        downgrading()
    elif Input == 5:
        lollipop()
    elif Input == 6:
        marsh()
    elif Input == 7:
        print("This feathure will no be implimented soon")
    elif Input == 8:
        load()
    elif Input == 9:
        root()
    else: 
        exit()

if __name__ == "__main__":
    start()