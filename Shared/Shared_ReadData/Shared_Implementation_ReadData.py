from PIL import Image
import pandas as pd 
import zope.interface 
from Shared_Interface_ReadData import readData
import os
import glob

@ zope.interface.implementer(readData)
class ReadData:
    def read_image_jpg(self, path, folder):
        # if image path contain a single image file, return 
        if folder == '':
            return Image.open(path).convert('RGB')
        # if image path is a directory, read images contained in it
        img_path = os.path.join(path, folder)
        img_collection = [Image.open(img).convert('RGB') for img in glob.glob(os.path.join(img_path, '*.jpg'))]
        return img_collection

    def read_image_png(self, path, folder):
        # if image path contain a single image file, return 
        if folder == '':
            return Image.open(path).convert('RGB')
        # if image path is a directory, read images contained in it
        img_path = os.path.join(path, folder)
        img_collection = [Image.open(img).convert('RGB') for img in glob.glob(os.path.join(img_path, '*.png'))]
        return img_collection

    