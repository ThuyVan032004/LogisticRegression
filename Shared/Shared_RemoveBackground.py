from rembg import remove
from PIL import Image
import os 
import glob

def removeBackground(folderPath, i, img_collection):
    for img in img_collection:
        output_path = folderPath + "\img_" + str(i) + ".png"
        output = remove(img)
        output.save(output_path)
        i += 1
