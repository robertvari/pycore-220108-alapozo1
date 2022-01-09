import os

photo_folder = r"C:\Work\_PythonSuli\pycore-220108\photos"
files = os.listdir(photo_folder)
photos = []
extensions = [".jpeg", ".jpg"]

for i in files:
    name, ext = os.path.splitext(i)

    if ext.lower() not in extensions:
        continue

    print(i)