import os
import shutil

#Define Funtions

def backUp(src):
    for word in src:
        source = word.replace("\n", "")
        destination = next(src).replace("\n", "")
        break
        
    #list all folders in the saves directory
    worldsList = os.listdir(source)
    for f in worldsList:
        print(f)
    print()    
    world = input("Enter the name of the world you want to back up exactly: ")
    print("Working...")
    
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


#Main code
def main():

    exists = fileExists()
    if exists:
        src = open("saveDirectory.txt", "r")
        backUp(src)
    else:
        setup()




main()