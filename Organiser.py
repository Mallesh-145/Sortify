# organiser.py
import shutil
import os
import config

def run():
    os.chdir(r"C:\Users\Mallesh\Downloads")
    items_lists = os.listdir()
    mapping = {}
    Order_list = config.get_categories()
    folders = Order_list.keys()

    for file in items_lists:
        filename, ext = os.path.splitext(file)
        for i in folders:
            folder = Order_list.get(i)
            if folder is not None and ext in folder:
                dst = os.path.join(os.getcwd(), i)
                src = os.path.abspath(file)
                shutil.move(src, dst)
