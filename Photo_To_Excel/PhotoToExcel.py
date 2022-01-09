import os
from PIL import Image, ExifTags
import json

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
photo_data = {}

for file in photos:
    photo_path = os.path.join(photo_folder, file)

    img = Image.open(photo_path)
    photo_data[file] = {
        "x": img.size[0],
        "y": img.size[1],
        "path": photo_path,
        "date": None,
        "camera": None,
        "iso": None
    }

    # get exif data
    exif_data = img._getexif()
    if not exif_data:
        continue

    for key, value in exif_data.items():
        tag_name = ExifTags.TAGS.get(key)
        print(tag_name, value)


    photo_data[file]["date"] = exif_data[306]


# create the photo_data.txt and write the data
data_file_path = os.path.join(photo_folder, "photo_data.json")
with open(data_file_path, "w") as f:
    json.dump(photo_data, f)