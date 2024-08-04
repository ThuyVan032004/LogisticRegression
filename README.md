# Dog Breeds Classification

This code is for classifying different breeds of dog. 

## Table of Contents
- Prerequisite
- Installation
- Usage 

## Prerequisite 
- Text Editor (ex: Visual Studio Code, Visual Studio...)
- Python
If you doesn't install Python, following these steps:
    1. Go to the official Python website ([click here](https://www.python.org/downloads/)) & Click on the download link for the latest version of Python
    2. Run the installer
        Make sure to check the box that says “Add Python to PATH”.
- Jupyter Notebook
    Run this command to install 
    ```
    pip install jupyter
    ```

## Installation
Run the following command to install packages

1. For Image processing: 
    - OpenCV 
    ```
    pip install opencv-python
    ```
    - PIL (Python Imaging Library):
    ```
    pip install pillow
    ```
    - rembg 
    ``` 
    pip install rembg
    ```
2. For Visualization:
    We will use Seaborn library. Run the following command to install Seaborn
    ```
    pip install seaborn
    ```
## Usage
Click on "Run All" in your Jupyter Notebook file to run the whole code once. After that, find the following code and comment them 
```
removeBackground(german_rembg, 1, german_shepherd_img)
removeBackground(golden_rembg, 1, golden_retriever_img)
``` 
```
removeBackground(rembg_german_path, 1, german_resized_imgs)
removeBackground(rembg_golden_path, 1, golden_resized_imgs)
```






