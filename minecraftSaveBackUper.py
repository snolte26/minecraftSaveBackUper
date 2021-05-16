import os
import shutil

def backUp(src):
    print()
    world = input("World name: ")
    for word in src:
        source = word.replace("\n", "")
        destination = next(src).replace("\n", "")
        break
    source = source + "\\" + world
    destination = destination + "\\" + world

    dest = shutil.copytree(source, destination)
    shutil.make_archive(destination, "zip", destination)



def fileExists():
    try:
        f = open("saveDirectory.txt")
        f.close()
        return True
        # Do something with the file
    except IOError:
        print("No Login Found")
        return False

def setup():
    print()
    saveDirectory = open("saveDirectory.txt", "w+")
    saves = input("Enter world saves directory (ex: C:\\Users\\Your_UserName\\AppData\\Roaming\\.minecraft\\saves): ") + "\n"
    desktop = input("Enter desktop directory (C:\\Users\\Your_UserName\\Desktop): ") + "\n"

    saveDirectory.writelines(saves)
    saveDirectory.writelines(desktop)

    backUp(saveDirectory)

def main():

    exists = fileExists()
    if exists:
        src = open("saveDirectory.txt", "r")
        backUp(src)
    else:
        setup()




main()