# file_operations.py
import os
import time
import shutil # File operations library
import glob # File and directory path manipulation
from text_to_speech import speak

# Reading files in Python
def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

# Writing files in Python
def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

# Reading file attributes in Python
def get_file_attributes(file_path):
    stat = os.stat(file_path)
    size = stat.st_size
    last_accessed = time.ctime(stat.st_atime)
    last_modified = time.ctime(stat.st_mtime)
    return size, last_accessed, last_modified

# Function to create a directory
def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        return f"Directory '{directory_name}' created successfully."
    except FileExistsError:
        return f"Directory '{directory_name}' already exists."
    except Exception as e:
        return f"Error creating directory: {str(e)}"

# Function to delete a file or directory
def delete_file_or_directory(path):
    try:
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
                speak(f"File '{path}' deleted successfully.")
            elif os.path.isdir(path):
                os.rmdir(path)
                speak(f"Directory '{path}' deleted successfully.")
        else:
            speak(f"'{path}' does not exist.")
    except PermissionError:
        speak(f"Permission denied. Unable to delete '{path}'.")
    except Exception as e:
        speak(f"Error deleting '{path}': {str(e)}")

# Function to search for a file or directory
def search_for_file_or_directory(name):
    results = []
    for root, dirs, files in os.walk(os.getcwd()):
        if name in dirs or name in files:
            results.append(os.path.join(root, name))
    return results if results else f"No match found for '{name}'."

# Function to get file properties
def get_file_properties(path):
    try:
        if os.path.exists(path):
            file_info = os.stat(path)
            size = file_info.st_size
            date_modified = datetime.datetime.fromtimestamp(file_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            permissions = oct(os.stat(path).st_mode & 0o777)
            return f"File: {path}\nSize: {size} bytes\nDate Modified: {date_modified}\nPermissions: {permissions}"
        else:
            return f"'{path}' does not exist."
    except Exception as e:
        return f"Error getting file properties: {str(e)}"

# Function to perform file searches in Python
def file_search(query):
    entries = glob.glob(query, recursive=True)
    return entries

# Function to copy a file
def copy_file(source, destination):
    shutil.copy(source, destination)

# 'Create File' Command
def create_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        speak(f"File '{file_name}' created successfully.")
    except Exception as e:
        speak(f"Error creating file '{file_name}': {str(e)}")
