import glob
import os

# This function corrects the filepaths for use in Python.
# Usage is mainly due to Windows using backslashes.

def correctPath(dli):
    returnlist = []
    for x in dli:
        newstr = x.replace("\\", "/")
        returnlist.append(newstr)

    return returnlist


# This function just gets all of the files based
# on the given directory as a string. Returns a 
# list of all files with their respective paths.

def get_files(file_dir):
    dirlist = []
    for name in glob.glob(file_dir + "/*"):
        dirlist.append(name)
        
    dirlist = correctPath(dirlist)

    file_list = []

    for paths in dirlist:
        if (os.path.isdir(paths)):
            new_list = get_files(paths)
            file_list = file_list + new_list
        else:
            file_list.append(paths)

    return file_list

