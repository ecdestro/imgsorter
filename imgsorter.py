#!/usr/bin/python3

from PIL import Image
import shutil
import os

files = os.listdir('.')
folders = ["portrait", "square", "landscape", "landscape/16x9"]
images = []
ratios = []

for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)

for file in files:
    if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
        imgfile = Image.open(file)
        images.append(imgfile)
        imgfile.close()
        
for image in images:
    width, height = image.size
    ratio = width / height
    ratios.append(ratio)

sorted_images = sorted(zip(images, ratios), key=lambda x: x[1])

for i, (image, _) in enumerate(sorted_images):
    if ratios[i] > 1.7 and ratios[i] < 1.8:
        shutil.move(images[i].filename, folders[3])
    elif ratios[i] < 1:
        shutil.move(str(images[i].filename), folders[0])
    elif ratios[i] == 1:
        shutil.move(str(images[i].filename), folders[1])
    elif ratios[i] > 1:
        shutil.move(str(images[i].filename), folders[2])
