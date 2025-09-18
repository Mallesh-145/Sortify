# config.py
"""
Configuration for Sortify: base path and file category mappings.
"""
import os

# Base path for the Downloads folder
BASE_PATH = r"C:\Users\Mallesh\Downloads"

# File categories: folder name -> list of extensions
# All extensions are stored in lowercase for normalization
FILE_CATEGORIES = {
    'Applications': ['.exe', '.msi'],
    'Video Files': ['.mp4', '.mkv', '.avi'],
    'Images': ['.jpg', '.jpeg', '.png', '.webp', '.mov'],
    'Documents': ['.pdf', '.docx', '.txt', '.srt'],
    'Scripts': ['.py', '.js', '.json', '.yaml'],
}

def get_categories():
    """Return the file category mapping."""
    return FILE_CATEGORIES


def create_folders():
    """Ensure each target category folder exists under BASE_PATH."""
    for category in FILE_CATEGORIES.keys():
        folder_path = os.path.join(BASE_PATH, category)
        # Only create if path doesn't exist
        if os.path.exists(folder_path):
            if os.path.isfile(folder_path):
                print(f" Cannot create folder '{category}'; a file with the same name exists.")
            else:
                # folder already exists
                continue
        else:
            os.makedirs(folder_path)
            print(f" Created folder: {folder_path}")


    


