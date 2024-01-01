# FileManager
Project that uses python automation and machine learning to walk an entire computer's file system and delete duplicates.

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
