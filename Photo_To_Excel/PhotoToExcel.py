import os
from PIL import Image

# open photo folder and list content
photo_folder = r"C:\Work\_PythonSuli\pycore-220108\photos"
files = os.listdir(photo_folder)


# filter files and folders and find images (.jpeg, .jpg)
extensions = [".jpeg", ".jpg"]
photos = []
for i in files:
    name, ext = os.path.splitext(i)

    if ext.lower() not in extensions:
        continue

    photos.append(i)

# open images with PIL == Pillow
photo_data = ""

for file in photos:
    photo_path = os.path.join(photo_folder, file)

    img = Image.open(photo_path)
    photo_data += f"{file} {img.size}\n"


# create the photo_data.txt and write the data
data_file_path = os.path.join(photo_folder, "photo_data.txt")
with open(data_file_path, "w") as f:
    f.write(photo_data)