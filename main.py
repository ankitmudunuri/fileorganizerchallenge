#################################
#                               #
# File Sorting Script in Python #
#                               #
#################################


import files_directory as fd
import files_sorter as fs

def main():
    filedir = input("Enter target directory: ")
    targetpath = input("Enter target path: ")
    delbool_input = input("Do you want to keep the files at the original source? (Yes or No): ")
    delbool_input = delbool_input.lower()
    delbool = False

    if (delbool_input == "yes"):
        delbool = False
    elif (delbool_input == "no"):
        delbool = True
        
    listoffiles = fd.get_files(filedir)
    fs.move_files(listoffiles, targetpath, delbool)

    

if __name__ == "__main__":
    main()