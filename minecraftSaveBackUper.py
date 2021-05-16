import os
import shutil

#Define Funtions

def zip(source, destination, world):
    # adds the world name to the source/destinations
    source = source + "\\" + world
    destination = destination + "\\" + world
    
    # copies the world to the desktop
    dest = shutil.copytree(source, destination)
    # creates a .zip of the world thats on the desktop
    shutil.make_archive(destination, "zip", destination)
    
    # closes the document after all is done
    src.close()


def backUp(src):
    
    # goes through the document, setting the source and
    # destination to the first and second line in the document
    for word in src:
        source = word.replace("\n", "")
        destination = next(src).replace("\n", "")
        # also takes the line breaks from each line. line breaks are 
        # considered part of the string so we must remove them
        break
        
    #list all folders in the saves directory
    print("Worlds Found:")
    worldsList = os.listdir(source)
    for f in worldsList:
        print(f)
    print()    
    world = input("Enter the name of the world you want to back up exactly: ")
    print("Working...")
    
    # Zip the chosen world onto the desktop
    zip(source, destination, world)
    
    



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
    desktop = input("Enter output directory (ex: C:\\Users\\Your_UserName\\Desktop): ") + "\n"
    game = input("Enter .minecraft directory (ex: C:\\Users\\Your_UserName\\AppData\\Roaming\\.minecraft): ") + "\n"
    
    # writes the saves and desktop variables to the document
    saveDirectory.writelines(saves)
    saveDirectory.writelines(desktop)
    saveDirectory.writelines(game)
    
    # closes the text document, then reopens as read only
    saveDirectory.close()
    saveDirectory = open("saveDirectory.txt", "r")
    
    # sends the document to backUp() function
    menu()
    #backUp(saveDirectory)

def menu():
    while True:
        print("What would you like to do?")
        print("1. Set Saves and Desktop locations")
        print("2. Back up a single world")
        print("3. Back up all worlds")
        print("69. Close program")
        print()
        option = int(input("Enter the number of your choice: "))
        
        # run the setup() function
        if option == 1:
            setup()
            
        # Open saveDirectory.txt in read only as src, and send it to backUp()
        if option == 2:
            src = open("saveDirectory.txt", "r")
            backUp(src)
            
        # error closes the program
        if option == 69: #69 nice
            askdhfjalohrg
        
        #loop to start of menu if an invalid option is selected
        print()
        print ("Please select a valid option.")
        print()

#Main code
def main():
    
    # runs the fileExists() function, and sets result to exists variable, Boolean
    exists = fileExists()
    
    if exists:
        menu()
        
    # if false, run the setup() function
    else:
        setup()



# Runs main function
main()
