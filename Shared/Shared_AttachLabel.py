import cv2
import numpy as np 

def attach_label(img_set, folder, X, y):
    set_len = len(img_set)
    for i in range(set_len):
        resized_img = cv2.resize(np.array(img_set[i]), (145, 145))
        X.append(resized_img.flatten())
        if folder == "German_Shepherd_rembg" or folder == "german_rembg":
            y.append(0)
        if folder == "Golden_Retriever_rembg" or folder == "golden_rembg":
            y.append(1)
    