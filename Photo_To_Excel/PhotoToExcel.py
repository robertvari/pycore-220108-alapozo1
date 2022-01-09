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
for file in photos:
    photo_path = os.path.join(photo_folder, file)

    img = Image.open(photo_path)
    print(file, img.size)