import os
import shutil
import random

"""
Python script that splits dataset into training, validation and test sets and generates a yaml file to train YOLOv8 model from Ultralytics.
"""

# get the data path, join with image and labels
data_path = "/home/its-joji/Documents/yolov8_synthetic_run/coco_data"
image_path = os.path.join(data_path, "images")
label_path = os.path.join(data_path, "labels")

# Define the output directories for yaml file creation
image_dirs = {
    "train": os.path.join(image_path, "train"),
    "val": os.path.join(image_path, "val"),
    "test": os.path.join(image_path, "test"),
}

label_dirs = {
    "train": os.path.join(label_path, "train"),
    "val": os.path.join(label_path, "val"),
    "test": os.path.join(label_path, "test"),
}
# Split images into training, validation and test sets
for split in [*image_dirs.values(), *label_dirs.values()]:
    os.makedirs(split, exist_ok = True)

image_files = [f for f in os.listdir(image_path) if f.endswith('.jpg')]

print(f"Found {len(image_files)} image files: {image_files[:10]}...")  # Print the first 10 image files for sanity check

# Shuffle images
random.seed(123)
random.shuffle(image_files)

# Define split sizes
total_size = len(image_files)
train_size = int(0.8 * total_size)
val_size = int(0.1 * total_size)
test_size = total_size - (train_size + val_size)

# Assign these files according to the type of split
train_set = image_files[:train_size]
val_set = image_files[train_size:train_size + val_size]
test_set = image_files[train_size + val_size:]

# Move the files
def move_files(file_list, split):
    for file in file_list:
        base_file_name = os.path.splitext(file)[0]
        image_set_files = os.path.join(image_path, file)
        label_set_files = os.path.join(label_path, base_file_name + ".txt")

        if os.path.exists(image_set_files):
            shutil.move(image_set_files, os.path.join(image_dirs[split], file))
        if os.path.exists(label_set_files):
            shutil.move(label_set_files, os.path.join(label_dirs[split], base_file_name + ".txt"))
            
move_files(train_set, "train")
move_files(val_set, "val")
move_files(test_set, "test")

print(f"Dataset successfully split into train, val and test sets.")