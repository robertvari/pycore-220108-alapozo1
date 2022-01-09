import os
from PIL import Image, ExifTags
import json
from openpyxl import Workbook


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
# collect data
photo_data = {}

# open excel sheet
workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "File Path"
sheet["B1"] = "Date"
sheet["C1"] = "Size"
sheet["D1"] = "Camera"
sheet["E1"] = "ISO"


for index, file in enumerate(photos):
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

    # add data to workbook
    sheet[f"A{index + 3}"] = photo_path
    sheet[f"C{index + 3}"] = str(img.size)

    # get exif data
    exif_data = img._getexif()
    if not exif_data:
        continue

    for key, value in exif_data.items():
        tag_name = ExifTags.TAGS.get(key)

        if tag_name == "Model":
            photo_data[file]["camera"] = value
            sheet[f"D{index+3}"] = value
        elif tag_name == "DateTime":
            photo_data[file]["date"] = value
            sheet[f"B{index + 3}"] = value
        elif tag_name == "ISOSpeedRatings":
            photo_data[file]["iso"] = value
            sheet[f"E{index + 3}"] = value

    photo_data[file]["date"] = exif_data[306]


# create the photo_data.txt and write the data
data_file_path = os.path.join(photo_folder, "photo_data.json")
with open(data_file_path, "w") as f:
    json.dump(photo_data, f)

# save excel file
excel_file_path = os.path.join(photo_folder, "photo_data.xlsx")
workbook.save(excel_file_path)