# FileManager
Project that uses python automation and machine learning to walk an entire computer's file system and delete duplicates.



===
## File and Directory Adapeter Objects:

> To create a File and Directory Adapter class object in Python, we can define a base class that encapsulates shared behaviors and properties of files and directories. Then, we can create specific classes for File and Directory that inherit from this base class and add their unique functionalities and attributes.

---
_So I will create an Adapter class that has the basic attributes and behaviors as both the file and directory objects._

Here's an example of how you might define such a class:

```python
import os
from datetime import datetime

class FileSystemAdapter:
    """Base class for file system objects."""

    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.creation_time = datetime.fromtimestamp(os.path.getctime(path))
        self.modification_time = datetime.fromtimestamp(os.path.getmtime(path))
        self.size = os.path.getsize(path)

    def is_directory(self):
        return os.path.isdir(self.path)

    def is_file(self):
        return os.path.isfile(self.path)

    def __str__(self):
        return f"Name: {self.name}, Created: {self.creation_time}, Modified: {self.modification_time}, Size: {self.size} bytes"

class File(FileSystemAdapter):
    """Class for file objects."""

    def __init__(self, path):
        super().__init__(path)
        if not self.is_file():
            raise ValueError(f"{path} is not a file.")

    # Add file-specific methods here
    def _determine_file_type(self, data_storage):
        """Store the file object in the appropriate storage object.
        (script or system_file)"""
        # Create the logic to check if the file is in an organized project
        # directory or if its in a random directory as a script.
        pass

    def move_script(self, file, directory):
        """Once file type is determined, move the script into the appropriate directory"""
        pass

    def move_system_file(self, file, directory):
        """Once file type is determined to be standard system file
        either do nothing or move to a directory that may be better"""
        pass

    def delete_duplicate_file(self, **files):
        """Check file specifications to insure that the files are
        duplicates. determine which file was modified last and
        delete the one that wasn't modified last"""
        pass

class Directory(FileSystemAdapter):
    """Class for directory objects."""

    def __init__(self, path):
        super().__init__(path)
        if not self.is_directory():
            raise ValueError(f"{path} is not a directory.")

    def list_contents(self):
        return os.listdir(self.path)

    # Add directory-specific methods here

# Example Usage
try:
    file = File('/path/to/some/file.txt')
    print(file)

    directory = Directory('/path/to/some/directory')
    print(directory)
    print("Contents:", directory.list_contents())

except ValueError as e:
    print(e)
```
In this implementation:

`FileSystemAdapter` is the base class that provides common functionalities and attributes like the path, name, creation time, modification time, and size of the file system object.

`File` and `Directory` are subclasses that extend `FileSystemAdapter`. They include checks to ensure the path provided is indeed a file or directory, respectively, and they can have additional methods specific to files or directories.

The `File` class can be extended with more file-specific functionalities as needed.

The `Directory` class includes a method list_contents to list the contents of the directory.

Remember to replace `/path/to/some/file.txt` and `/path/to/some/directory` with actual paths on your system to test this code. Also, this code does not handle all possible edge cases and error conditions that might arise in a full-scale application, so you may need to add more robust error handling for production use.


===
## File Sorting and Cleaning:

To recursively sort through an entire computer directory system and organize .git directories and standalone scripts, you would typically write a script in a language like Python or Bash. Here's a high-level approach in Python:

Scan for .git Directories:

Recursively walk through the directories starting from a specified root directory.
For each directory, check if it contains a .git folder.
If a .git folder is found, move the directory containing the .git folder to the dev/projects folder.
Find and Move Standalone Scripts:

Again, recursively walk through the directories.
For each file, check if it's a script (e.g., by extension like .py, .sh).
If it's a standalone script (not part of a project with a .git directory), move it to the dev/scripts folder.
A simple Python script might look like this:

```python
import os
import shutil

def move_git_directories(root_dir, projects_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '.git' in dirnames:
            shutil.move(dirpath, projects_dir)
            dirnames.remove('.git')  # prevent further walking into this directory

def move_scripts(root_dir, scripts_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith('.py') or file.endswith('.sh'):  # Add other script types if needed
                shutil.move(os.path.join(dirpath, file), scripts_dir)

root_directory = '/path/to/your/main/directory'
projects_directory = '/path/to/dev/projects'
scripts_directory = '/path/to/dev/scripts'

move_git_directories(root_directory, projects_directory)
move_scripts(root_directory, scripts_directory)

```

> #### Important Notes:

> Backup your data before running such a script, as it can potentially move a lot of files and directories around.

> Modify the script to suit your specific needs, such as handling different types of scripts or adding more checks.

> Be careful with permissions and make sure the script is run with the appropriate level of access.

> Test the script on a small, controlled directory first to ensure it behaves as expected.


===
## Finding File Owner Information:

> __To search for files on a disk that were created by you and not by the system using Python, you would typically follow these steps:__

1.) __Identify User Files:__ Determine criteria to differentiate between your files and system files. This might include looking at file locations, creation dates, file types, or specific metadata.

2.) __Use Python Libraries:__ Utilize libraries such as `os`, `os.path`, and `pathlib` to navigate the file system and retrieve file information.

3.) __Filter Files:__ Apply the identified criteria to filter out system files.

Here's an example script that searches for files in a specified directory (and its subdirectories) based on the file owner. This script assumes that files created by you have your user ID as the owner. We'll use the os and `pathlib` libraries:


```python
import os
import pathlib
from pwd import getpwuid  # Note: pwd module is Unix-specific

def get_file_owner(file_path):
    """ Get the owner of the file. """
    try:
        return getpwuid(os.stat(file_path).st_uid).pw_name
    except Exception as e:
        print(f"Error getting owner for file {file_path}: {e}")
        return None

def find_user_files(start_path, user_name):
    """ Find files created by the specified user. """
    user_files = []
    for path in pathlib.Path(start_path).rglob('*'):
        if path.is_file():
            owner = get_file_owner(path)
            if owner == user_name:
                user_files.append(str(path))
    return user_files

# Replace '/your/directory' with the path you want to search
# Replace 'your_username' with your actual username
user_files = find_user_files('/your/directory', 'your_username')

for file in user_files:
    print(file)
```

===
## Adding Additional Functionality:


_To add functionality for checking duplicates before moving directories or scripts, you can modify the script as follows:_

_Create a function to check for duplicates:_

> This function will take a file or directory path and a target directory, and check if an item with the same name already exists in the target directory.
Modify the moving functions to use this check:

> Before moving a directory or script, call the duplicate check function.
If a duplicate is found, decide on an action (e.g., skip, rename, or merge).


__Here's how the modified Python script might look:__


```python
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
            dirnames.remove('.git')  # prevent further walking into this directory

def move_scripts(root_dir, scripts_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith('.py') or file.endswith('.sh'):  # Add other script types if needed
                full_file_path = os.path.join(dirpath, file)
                if not is_duplicate(full_file_path, scripts_dir):
                    shutil.move(full_file_path, scripts_dir)

root_directory = '/path/to/your/main/directory'
projects_directory = '/path/to/dev/projects'
scripts_directory = '/path/to/dev/scripts'

move_git_directories(root_directory, projects_directory)
move_scripts(root_directory, scripts_directory)
```

> __Handling Duplicates:__

- In this script, if a duplicate is found, the item is simply not moved. You can modify this behavior to rename the item, merge directories, or even prompt the user for action.

- Ensure that the is_duplicate function checks accurately, considering cases like case sensitivity in filenames on different operating systems.

- Always test such scripts in a controlled environment to prevent accidental data loss or overwrite.

===

> _Storing the path of each project before moving it can be an effective strategy to handle duplicates. This approach allows you to compare the current directory with the stored paths, helping you decide how to handle potential duplicates. Here's how you can incorporate this into your script:_

> ##### 1.) Store Paths in a Set or Dictionary:
- Before moving any directories, you can store their paths in a set or dictionary. This allows for quick lookup and comparison when you encounter a directory with the same name later in the process.
> ##### 2.) Modify the Move Function:
- When moving a directory, check if its path is in the set or dictionary. If it is, handle the duplicate as needed (skip, merge, rename, etc.).

> ##### 3.) Update the Set or Dictionary After Moving:
- Once a directory is successfully moved, update the set or dictionary with its new location.


> _Here's an updated version of the script incorporating these changes:_

```python
import os
import shutil

def is_duplicate(source, target_dir, moved_paths):
    source_name = os.path.basename(source)
    target_path = os.path.join(target_dir, source_name)
    return os.path.exists(target_path) or target_path in moved_paths

def move_git_directories(root_dir, projects_dir, moved_paths):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '.git' in dirnames:
            if not is_duplicate(dirpath, projects_dir, moved_paths):
                shutil.move(dirpath, projects_dir)
                moved_paths.add(os.path.join(projects_dir, os.path.basename(dirpath)))
            dirnames.remove('.git')  # prevent further walking into this directory

root_directory = '/path/to/your/main/directory'
projects_directory = '/path/to/dev/projects'
scripts_directory = '/path/to/dev/scripts'

moved_paths = set()  # Keep track of moved project directories
move_git_directories(root_directory, projects_directory, moved_paths)
# move_scripts function can be similarly updated if needed
```

> __Considerations:__

- This script keeps track of moved directories but does not handle script files. If you need similar functionality for scripts, you should extend the `moved_paths` logic to them as well.

- Decide on a strategy for handling duplicates (skip, merge, rename) and implement it in the script.

- Always test the script in a safe environment to ensure it behaves as expected and to avoid data loss.

===
## Deep Learning Frameworks (Choose One):

`TensorFlow` (with `Keras`): A comprehensive and flexible framework that is widely used in the industry and academia. `Keras`, which is part of TensorFlow, provides a high-level API that is user-friendly.
`PyTorch`: Known for its ease of use and dynamic computational graph, `PyTorch` is popular in research and is gaining traction in industry applications.
Image Processing:

`Pillow` (PIL): A Python Imaging Library used for opening, manipulating, and saving many different image file formats. It's useful for basic image processing tasks.
OpenCV: Offers more advanced image processing capabilities than PIL and is particularly useful for real-time image processing.
Pre-trained Models for Image Classification and Object Detection:

`ImageNet` Pre-trained Models: Both TensorFlow/Keras and `PyTorch` offer models that have been pre-trained on ImageNet, a large visual database designed for use in visual object recognition software research. These models can classify images into numerous categories.
Face Recognition Models: For recognizing individuals in images, you can use specialized models like OpenFace or libraries like face_recognition (which uses dlib).
File Manipulation:

`os` or `pathlib`: For traversing directories and handling file paths.
`shutil`: Useful for moving files to different directories.
Here's a high-level outline of the steps you would take:

Set Up the Neural Network: Choose a pre-trained model suitable for your task. For general image classification, models like ResNet, VGG, or Inception could be appropriate. For face recognition, use a dedicated face recognition model.

Pre-process the Images: Use Pillow or OpenCV to resize and format the images as needed by your chosen neural network model.

Classify the Images: Run the images through the neural network to classify them or recognize faces.

Sort and Move Images: Based on the classification results, use Python's file manipulation capabilities to sort the images into subdirectories.

Here's a basic pseudo-code outline:

```python
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import numpy as np
import os
import shutil

# Load pre-trained ResNet50 model
model = ResNet50(weights='imagenet')

def classify_image(img_path):
    # Load image
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Classify image
    preds = model.predict(x)
    return decode_predictions(preds, top=1)[0][0]

def sort_images(source_directory, destination_base_directory):
    for subdir, dirs, files in os.walk(source_directory):
        for file in files:
            try:
                # Classify each image
                result = classify_image(os.path.join(subdir, file))
                category = result[1]  # or any other logic for subdirectory name

                # Create target directory if it doesn't exist
                target_directory = os.path.join(destination_base_directory, category)
                os.makedirs(target_directory, exist_ok=True)

                # Move file
                shutil.move(os.path.join(subdir, file), target_directory)
            except Exception as e:
                print(f"Error processing {file}: {e}")

source_directory = '/path/to/source'
destination_directory = '/path/to/destination'
sort_images(source_directory, destination_directory)
```

Important Considerations:

The accuracy of classification and face recognition depends on the quality and diversity of the training data used in the pre-trained models.
Be aware of privacy and ethical considerations, especially when dealing with facial recognition.
This is a high-level outline; you'll need to tailor the code to your specific needs, especially the logic for naming and creating subdirectories based on classification results.
Always test on a small set of data before scaling up.
