import os
import time
import shutil

#Define Funtions

def backUp(src):
    exit = False
    while True:
        # clears the console
        os.system('cls')

        print("Choose one: ")
        print()
        print("1. Back up a world")
        print("2. Back up all worlds")
        print("3. Exit")
        choice = int(input())

        # goes through the document, setting the source and
        # destination to the first and second line in the document
        for word in src:
            source = word.replace("\n", "")
            destination = next(src).replace("\n", "")
            # also takes the line breaks from each line. line breaks are
            # considered part of the string so must remove them
            break

        if choice >= 1 and choice <= 3:
            if choice == 1:
                os.system('cls')

                # list all folders in the saves directory
                print("Worlds Found:")
                worldsList = os.listdir(source)
                worldsListing = []
                for f in worldsList:
                    worldsListing.append(f)
                    print(worldsListing.index(f), ": ", f)
                print()
                worldo = int(input("Enter World number: "))
                print("Working...")
                world = worldsListing[worldo]

                # adds the world name to the source/destinations
                sources = source + "\\" + world
                destinations = destination + "\\" + world

                # copies the world to the desktop
                dest = shutil.copytree(sources, destinations)
                # creates a .zip of the world that's on the desktop
                shutil.make_archive(destinations, "zip", destinations)
                print("Done")
                # sleeps for 5 seconds before clearing and starting over
                time.sleep(5)
            elif choice == 2:
                print("Working...")

                worldsList = os.listdir(source)
                for f in worldsList:
                    srcs = source + "\\" + f
                    des = destination + "\\" + f

                    # copies the world to the desktop
                    dest = shutil.copytree(srcs, des)
                    # creates a .zip of the world that's on the desktop
                    shutil.make_archive(des, "zip", des)
                print("Done")
                # sleeps for 5 seconds before clearing and starting over
                time.sleep(5)


            else:
                exit = True
        else:
            print("Pick an option, 1 or 2")
            continue
        if exit:
            break
        else:
            continue
    # closes the document after all is done
    src.close()



def fileExists():
    # tries to open the document
    try:
        f = open("saveDirectory.txt")
        f.close()
        return True
        # if successful, return True
    except IOError:
        print("No Directories Found")
        return False
        # if unsuccessful, return false
        # prevents program from throwing a hissy fit and going out to lunch

def setup():
    
    # Create a new text document, saveDirectory.txt, to write to it
    saveDirectory = open("saveDirectory.txt", "w+")
    
    # set the world save directory to the user input with a line break
    # same with desktop directory
    saves = input("Enter world saves directory (ex: C:\\Users\\Your_UserName\\AppData\\Roaming\\.minecraft\\saves): ") + "\n"
    desktop = input("Enter desktop directory (C:\\Users\\Your_UserName\\Desktop): ") + "\n"
    
    # writes the saves and desktop variables to the document
    saveDirectory.writelines(saves)
    saveDirectory.writelines(desktop)
    
    # closes the text document, then reopens as read only
    saveDirectory.close()
    saveDirectory = open("saveDirectory.txt", "r")
    
    # sends the document to backUp() function
    backUp(saveDirectory)


#Main code
def main():
    
    # runs the fileExists() function, and sets result to exists variable, Boolean
    exists = fileExists()
    # If true, open saveDirectory.txt in read only as src, and send it to backUp()
    if exists:
        src = open("saveDirectory.txt", "r")
        backUp(src)
    # if false, run the setup() function
    else:
        setup()



# Runs main function
main()
