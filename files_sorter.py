import os
import shutil

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
            new_filepath = new_filepath[-1]
            new_filepath = inp_path + "/" + new_filepath
            if delbool == False:
                shutil.copy(x, new_filepath)
            else:
                shutil.move(x, new_filepath)

