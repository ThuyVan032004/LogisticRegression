import cv2
import pandas as pd 
import zope.interface 
from Shared_Interface_ReadData import readData
import os
import glob

@ zope.interface.implementer(readData)
class ReadData:
    def read_csv(self, filepath):
        return pd.read_csv(filepath)
    def read_image(self, path, folder):
        # if image path contain a single image file, return 
        if folder == '':
            return cv2.imread(path)
        # if image path is a directory, read images contained in it
        img_path = os.path.join(path, folder)
        img_collection = [cv2.imread(img) for img in glob.glob(os.path.join(img_path, '*.jpg' or '*.png'))]
        return img_collection
