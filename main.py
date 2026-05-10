from pathlib import Path
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
        if not p.exists():
            with open(p,"w") as f:
                write = input("Enter the content you want to write in the file: ")
                f.write(write)
            print(F"{filename} created successfully")  
        else:
            print(f"File {filename} already exists.")
    except Exception as err:
        print(f"Error: {err}")  





print("press 1 for create a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("enter your choice: "))

if check == 1:
    createfile()