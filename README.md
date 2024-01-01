# FileManager
Project that uses python automation and machine learning to walk an entire computer's file system and delete duplicates.



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
