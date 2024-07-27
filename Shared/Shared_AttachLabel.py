import cv2

def attach_label(img_set, folder, X, y):
    set_len = len(img_set)
    for i in range(set_len):
        resized_img = cv2.resize(img_set[i], (140, 140))
        X.append(resized_img.flatten())
        if folder == "German_Shepherd":
            y.append(0)
        if folder == "Golden_Retriever":
            y.append(1)