import os
import shutil

# Function to organize files into folders with the same name
def organize_files_in_folders(directory):
    # Loop through each file in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file name without the extension
            folder_name = os.path.splitext(file_name)[0]
            
            # Create the folder path
            folder_path = os.path.join(directory, folder_name)
            
            # Create the folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)
            
            # Move the file into the new folder
            shutil.move(file_path, os.path.join(folder_path, file_name))
            print(f"Moved: {file_name} to folder: {folder_name}")

# Specify the directory containing the files
directory_to_process = "C:/Users/Ironm.RC-LENOVO/Videos/"
organize_files_in_folders(directory_to_process)