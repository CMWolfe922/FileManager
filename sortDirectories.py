import os
import shutil

def is_python_project(dir_path):
    # Check for Python project indicators
    return any(file in os.listdir(dir_path) for file in ['requirements.txt', 'setup.py'])

def is_nodejs_project(dir_path):
    # Check for Node.js project indicator
    return 'package.json' in os.listdir(dir_path)

def move_projects(start_path, target_path):
    for root, dirs, files in os.walk(start_path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if is_python_project(dir_path) or is_nodejs_project(dir_path):
                shutil.move(dir_path, target_path)
                print(f'Moved {dir_path} to {target_path}')

# Set your paths here
start_directory = '/path/to/search'
target_directory = '/path/to/move/projects'

move_projects(start_directory, target_directory)