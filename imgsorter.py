#!/usr/bin/python3

#!/usr/bin/python

import os
import shutil
import PIL.Image

def sort_images_by_aspect_ratio(image_folder):

    aspect_ratio_folders = {
        "landscape": os.path.join(image_folder, "landscape"),
        "landscape/16x9": os.path.join(image_folder, "landscape/16x9"),
        "landscape/16x10": os.path.join(image_folder, "landscape/16x10"),
        "portrait": os.path.join(image_folder, "portrait"),
        "misc": os.path.join(image_folder, "misc"),
        "misc/gif": os.path.join(image_folder, "misc/gif"),
        "misc/webp": os.path.join(image_folder, "misc/webp"),
        "square": os.path.join(image_folder, "square")
    }

    for folder_name in aspect_ratio_folders.values():
        os.makedirs(folder_name, exist_ok=True)

    for image_file in os.listdir(image_folder):
        if image_file.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(image_folder, image_file)
            image = PIL.Image.open(image_path)
            width, height = image.size
            aspect_ratio = width / height

            if aspect_ratio == 1.6:
                destination_folder = aspect_ratio_folders["landscape/16x10"]
            elif aspect_ratio > 1.7 and aspect_ratio < 1.8:
                destination_folder = aspect_ratio_folders["landscape/16x9"]
            elif aspect_ratio < 1:
                destination_folder = aspect_ratio_folders["portrait"]
            elif aspect_ratio == 1:
                destination_folder = aspect_ratio_folders["square"]
            elif aspect_ratio > 1:
                destination_folder = aspect_ratio_folders["landscape"]

            new_path = os.path.join(destination_folder, image_file)
            image.close()
            shutil.move(image_path, new_path)

if __name__ == "__main__":
    image_folder = "."
    sort_images_by_aspect_ratio(image_folder)
