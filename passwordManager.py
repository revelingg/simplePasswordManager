import time 
from cryptography.fernet import Fernet


#Ibukun Adenuga
#7/4/23
# Password manager that hashes user passwords and uses SQL for storage

#need to import the :
    #user
    #website
    #store and encrypt the passwords into a diff file

'''
#function that generated a key 
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as keyFile:
        keyFile.write(key)
    '''


def loadKey():
    #opens closes and returns the key 
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key 
    


def men():
   #menu options  
    print("MENU: \n")
    print(f"1. Add a new password \n2. Remove an old password \n3. Check current Passwords \n4. Edit a Current Password \n5. Quit\n")
    print("Remeber the file format is : User | Website | Password\n\n")



def menu():
    men()
    #calls the menu checks the choice and if its not an integer it calls it again 
    while True:
        try:
            choice = int(input("What would you like to do?: "))
            if choice < 1 or choice > 5:
                print()
                print("Error. Invalid Option. Try Again")
                print()
                men()
            else:
                break  # Valid input, exit the loop
        except ValueError:
            print()
            print("Error. Invalid Option. Try Again")
            print()
            men()
    return choice




def actions(choice, path ):
    
   
    print()
    
    #if choice is one enter the information access it thru the tuple thats returned set the new variables again and then write them to the file
    
    if choice == 1:
        username = str(input("Enter your username ( if none input N/A): "))
        print()
        website = str(input("Enter the website  ( if none input N/A): "))
        print()
        password = str(input("Enter your password ( if none input N/A): "))
        print()

        set = process_input(username, website, password)
        #set is a variable that stories the tuple and is then accessed by these 

        username = set[0]
        website = set[1]
        password = set[2]
      

        with open(path, "a") as file:
            
            file.write(f"{username} | {website} | {password}\n")
        print("\n\n\n")
        time.sleep(2.5)
    


    elif choice == 2:
        #deletes a password line 
        time.sleep(1)
        print("Here are Your Current Sites and Passwords: \n\n")
        with open(path, "r") as file:
            i = 1
            
            lines = []
            for line in file:
               
                line = line.rstrip('\n')
                print(f"{i}. {line}")
                lines.append(line)
                i = i+1

        print("\n\n")
        opt = int(input("Which line  would you like to delete: "))
        s = True
        while s:
            if opt < 1 or opt > len(lines):
                print("\nInvalid line option. Retry. \n")
                opt = int(input("Which line  would you like to delete: "))
            else:
                s = False
               
               
                print()
               
                lines.remove(lines[opt-1])
                with open(path, "w" ) as file:
                    for line in lines:
                        file.write(f"{line}\n")
                    print("\nHeres the new Passwords File: \n\n")
                    i = 1
           
                    for line in lines:
                        line = line.rstrip('\n')
                        print(f"{i}. {line}")
                        i = i+1
                    print()


            
               
        time.sleep(2.5)
         
    elif choice == 3:
        # View all current password lines
        with open(path, "r") as file:
            i = 1
           
            for line in file:
                line = line.rstrip('\n')
                print(f"{i}. {line}")
               
                i = i+1

        print("\n\n\n")
        time.sleep(2.5)

        
    elif choice == 4:
        time.sleep(1)
        print("Here are Your Current Sites and Passwords: \n\n")
        with open(path, "r") as file:
            i = 1
            lines = []
            for line in file:
                line = line.rstrip('\n')
                print(f"{i}. {line}")
                lines.append(line)
                i = i+1

        print("\n\n")
        opt = int(input("Which line  would you like to edit: "))
        s = True
        while s:
            if opt < 1 or opt > len(lines):
                print("\nInvalid line option. Retry. \n")
                opt = int(input("Which line  would you like to edit: "))
            else:
                s = False
                print("\nRemeber the line format is : User | Website | Password\n")
                new_line = input("\nEnter the updated line: ")
                print()
               
                lines[opt - 1] = new_line
                with open(path, "w") as file:
                    for line in lines:
                        file.write(f"{line}\n")
        time.sleep(2.5)
    else:
        print("Bye!\n\n")
        time.sleep(2.5)


      
    
           
   



def process_input(username, website, password):
    #checks if any of the fields are N/A and returns a tuple
    if username.lower() == 'n/a':
        username = None
    if website.lower() == 'n/a':
        website = None
    if password.lower() == 'n/a':
        password = None
    return username, website, password





def checkFile():
    #checks if the file exists and processes it
    fileName = input("What would you like to name your storage file?: ")
    val = True
    path = (f"C:\\Users\\ibuku\\OneDrive\\Desktop\\Documents\\CyberProjects\\PassManager\\{fileName}.txt")
    mode = "a"

    while val:
        try:
            file = open(path, mode)
            print("\nFile created successfully!")

            val = False
            file.close() 
        except FileNotFoundError:
            print("\nERROR -- There is an issue with file {path}. Please reenter:")
    return path 





def main():
    USER = input("\n\nWho owns this manager?: ")
    #MASTERPW = str(input(f"\nWelcome {USER} what will be the master password to access your files?: "))

    #key = loadKey() + MASTERPW.encode()
    #finalkey = Fernet(key)
   
    print()
    storageFile = checkFile()
    print()

   
    
   
    print()

    print(f"\n\nWelcome to {USER}'s password manager\n")
    choice = 0
    while choice != 5:
        
        choice = menu()
       
        actions(choice, storageFile)
    







main()
