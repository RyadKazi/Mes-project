# File copier
import os
import shutil

def copier(fichier, destin, name):
    ext = os.path.splitext(fichier)[1]
    name_with_ext = str(f"{name}{ext}")
    try:
        if os.path.exists(os.path.join(destin, name_with_ext)):
            print("That name already exists, change it!!")
            choice()
        else:
            new_path = str(os.path.join(destin, name_with_ext))
            shutil.copy(str(fichier), new_path)
    except FileExistsError:
        print("That file does not exist")
    except PermissionError:
        print("This file is not allowed to be copied")
    else:
        choice()


# ======================================================================================================

def choice():
    x = ""
    while True:
        x = input("Enter a 'q' to quit or 'r' to restart: ").lower()
        if (x == "q") or (x == "r"):
            break
    if x == "q":
        return ("q")
    elif x == "r":
        start()


# ======================================================================================================

def start():
    file = input("Enter the file you want to copy: ")
    destination = input("To the destination of: ")
    nom = input("By the name of:")

    copier(file, destination, nom)

start()
