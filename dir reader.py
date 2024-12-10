#Directory Reader
import os
def list_dir(folder):
        try:
            for file_or_folder in os.listdir(folder):      #Cheks for files or folders in the folder
                if os.path.isfile(os.path.join(folder,file_or_folder)):      #checks if is it a file base on the path
                    print(file_or_folder)
                if os.path.isdir(os.path.join(folder,file_or_folder)):     #checks if is it a folder
                    print(f"{file_or_folder} (folder)")
            print("The operation was done successfully")
        except PermissionError:
            print("Error, There's is no permission to enter this folder")
        except IsADirectoryError:
            print("This operation doesn't work on a directory")
        except NotADirectoryError:
            print("This path is not for a directory")

#====================================================================================================

def start():
    folder_path = input("Enter a folder path you want to list its files: ")
    list_dir(folder_path)
start()

#====================================================================================================