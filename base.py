# base.py
import os
import textwrap
import config

def run():
    MaX_Name_Value = 30
    os.chdir(r"C:\Users\Mallesh\Downloads")
    items_lists = os.listdir()
    mapping = {}

    for file in items_lists:
        if os.path.isfile(file):
            mapping[file] = "File"
        if os.path.isdir(file):
            mapping[file] = "Folder"

    print(f"The files and folders in the downloads are ........")
    print("S no     File Name                               Extension                    Type")
    for idx, (filename,item_type) in enumerate(mapping.items(),start=1):
        filename, extension = os.path.splitext(filename)
        if extension == "":
            extension = "  -"
        lines = textwrap.wrap(filename,width=MaX_Name_Value) or [""]
        print(f"{idx:<5} {lines[0]:<35} {extension:<10} {item_type}")
        for extra in lines[1:]:
            print(f"{'':<5} {extra:<35} {'':<10} {''}")
