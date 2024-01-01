from datetime import datetime
from collections import defaultdict
import hashlib
import os
import shutil

import os
import shutil


def is_duplicate(source, target_dir):
    source_name = os.path.basename(source)
    target_path = os.path.join(target_dir, source_name)
    return os.path.exists(target_path)


def move_git_directories(root_dir, projects_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '.git' in dirnames:
            if not is_duplicate(dirpath, projects_dir):
                shutil.move(dirpath, projects_dir)
            # prevent further walking into this directory
            dirnames.remove('.git')


def move_scripts(root_dir, scripts_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            # Add other script types if needed
            if file.endswith('.py') or file.endswith('.sh'):
                full_file_path = os.path.join(dirpath, file)
                if not is_duplicate(full_file_path, scripts_dir):
                    shutil.move(full_file_path, scripts_dir)


root_directory = '/path/to/your/main/directory'
projects_directory = '/path/to/dev/projects'
scripts_directory = '/path/to/dev/scripts'

move_git_directories(root_directory, projects_directory)
move_scripts(root_directory, scripts_directory)



def get_file_hash(file_path):
    """Generate a hash for a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()


def is_programming_project(dir_path):
    """Check if a directory is a programming project."""
    # Define logic to determine if a directory is a programming project
    # E.g., check for certain file types, project files, etc.
    pass


def is_script(file_path):
    """Check if a file is a programming script."""
    # Define logic to determine if a file is a script
    # E.g., file extension checks (.py, .js, etc.)
    pass


def is_image(file_path):
    """Check if a file is an image."""
    # Define logic to determine if a file is an image
    # E.g., file extension checks (.jpg, .png, etc.)
    pass


def find_items(root_path):
    projects = []
    scripts = []
    images = []

    for root, dirs, files in os.walk(root_path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if is_programming_project(dir_path):
                projects.append(dir_path)

        for file in files:
            file_path = os.path.join(root, file)
            if is_script(file_path):
                scripts.append(file_path)
            elif is_image(file_path):
                images.append(file_path)

    return projects, scripts, images


def remove_duplicates(items):
    seen_hashes = defaultdict(list)
    for item in items:
        file_hash = get_file_hash(item)
        seen_hashes[file_hash].append(item)

    for file_list in seen_hashes.values():
        file_list.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        for file in file_list[1:]:
            os.remove(file)


def main():
    root_path = input("Enter the path to search: ")
    projects, scripts, images = find_items(root_path)

    remove_duplicates(projects)
    remove_duplicates(scripts)
    remove_duplicates(images)

    print("Duplicates removed, remaining items:")
    print("Projects:", projects)
    print("Scripts:", scripts)
    print("Images:", images)


if __name__ == "__main__":
    main()
