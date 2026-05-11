from pathlib import Path
import os 
def readfilefolder():
    path = Path('')
    items = list(path.glob('*'))
    for i,items in enumerate(items):
        print(f"{i}--{items}")


def createfile():
    try:
        readfilefolder()
        filename = input("Enter the file name you want to create: ")
        p = Path(filename)
        if not p.exists() :
            with open(p,"w") as f:
                write = input("Enter the content you want to write in the file: ")
                f.write(write)
            print(F"{filename} created successfully")  
        else:
            print(f"File {filename} already exists.")
    except Exception as err:
        print(f"Error: {err}")  
def readfile():
    try:
        readfilefolder()
        filename = input("Enter the file name you want to read: ")
        p = Path(filename)
        if not p.exists() and p.is_file():
            with open(p,'r') as f:
                data = f.read()
                print(data)
                print(f"{filename} read successfully")
        else:
            print(f"File {filename} does not exist.")        
    except Exception as err:
        print(f"Error: {err}")  
def updatefile():
    try:
        readfilefolder()
        filename = input("Enter the file name you want to update: ")
        p = Path(filename)
        if p.exists() and p.is_file():
            print("Press 1 for rename the file")
            print("Press 2 for overwrite the file content")
            print("Press 3 for append the file content")
            enter = int(input("Enter your choice: "))
            if enter == 1:
                newname = input("Enter the new name of the file:")
                p2 = Path(newname)
                p.rename(p2)
                print(f"{filename} renamed to {newname} successfully")

            if enter == 2:
                with open(p,'w') as f:
                    data = input("Enter the new content you want to write in the file: ")
                    f.write(data)
                print(f"{filename} content overwritten successfully")  
            if enter == 3:
                with open(p,'a') as f:
                    data = input("Enter the content you want to append in the file: ")
                    f.write(" " + data)
                print(f"{filename} content appended successfully") 
    except Exception as err:
        print(f"Error: {err}")                 

def deletefile():
    try:
        readfilefolder()
        filename = input("Enter the file name you want to delete: ")
        p = Path(filename)
        if p.exists() and p.is_file():
            os.remove(p)
            print(f"{filename} deleted successfully")
        else:
            print(f"File {filename} does not exist.")
    except Exception as err:
        print(f"Error: {err}")        


print("press 1 for create a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("enter your choice: "))

if check == 1:
    createfile()
if check == 2:
    readfile()
if check == 3:
   updatefile() 
if check == 4:
    deletefile()    