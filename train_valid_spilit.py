# yolo_training/
# │
# ├── data/
# │   ├── train/
# │   │   ├── images/           # Training images
# │   │   └── labels/           # Training labels (annotations)
# │   │
# │   └── test/
# │       ├── images/           # Testing images
# │       └── labels/


import os
import shutil
import random

# Define paths
data_dir = r'C:\Users\rohin\Desktop\New folder (2)\trdp\datasets\yolov8_format'
images_dir = os.path.join(data_dir, 'images')
labels_dir = os.path.join(data_dir, 'annotations')

train_dir = os.path.join(data_dir, 'train')
train_images_dir = os.path.join(train_dir, 'images')
train_labels_dir = os.path.join(train_dir, 'annotations')

test_dir = os.path.join(data_dir, 'test')
test_images_dir = os.path.join(test_dir, 'images')
test_labels_dir = os.path.join(test_dir, 'annotations')

# Create directories if they don't exist
for directory in [train_dir, train_images_dir, train_labels_dir, test_dir, test_images_dir, test_labels_dir]:
    os.makedirs(directory, exist_ok=True)

# List all images
images = os.listdir(images_dir)
random.shuffle(images)

# Calculate split indices
train_split = int(0.8 * len(images))

# Split images and labels
train_images = images[:train_split]
test_images = images[train_split:]

# Move images to respective directories
for image in train_images:
    shutil.move(os.path.join(images_dir, image), os.path.join(train_images_dir, image))
    shutil.move(os.path.join(labels_dir, image[:-4] + '.txt'), os.path.join(train_labels_dir, image[:-4] + '.txt'))

for image in test_images:
    shutil.move(os.path.join(images_dir, image), os.path.join(test_images_dir, image))
    shutil.move(os.path.join(labels_dir, image[:-4] + '.txt'), os.path.join(test_labels_dir, image[:-4] + '.txt'))

print("Data split completed successfully!")
