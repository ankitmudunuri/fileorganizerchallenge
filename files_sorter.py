import os
import shutil

# This function actually moves the files depending on
# the filepath and the target path. It copies it and
# keeps the file in the original path if the delbool
# input is false, but moves it and deletes the original
# source if it is true.

def sort_folder(orig_path, file, inp_path, delbool):

    file_ext = file.split(".")
    file_ext = file_ext[-1]
    inp_path_check = inp_path + "/" + file_ext
    if not (os.path.isdir(inp_path_check)):
        os.mkdir(inp_path_check)
    if delbool == False:
        shutil.copy(orig_path, (inp_path_check + "/"))
    else:
        shutil.move(orig_path, (inp_path_check + "/"))

# This file facilitates the moving procedure of all of the files.
# It gets the filename and makes sure that the main target directory
# is present. 
# 
# If given more time or another chance to redo challenge, I would want 
# to make this function a bit cleaner with another function to pass off
# some of the reused code to.

def move_files(lop, inp_path, delbool=False):
    if (os.path.isdir(inp_path)):
        for x in lop:
            new_filepath = x.split("/")
            filepath = new_filepath[-1]
            sort_folder(x, filepath, inp_path, delbool)

    else:
        os.mkdir(inp_path)
        for x in lop:
            new_filepath = x.split("/")
            filepath = new_filepath[-1]
            sort_folder(x, filepath, inp_path, delbool)
            

