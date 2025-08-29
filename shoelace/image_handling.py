import cv2 as cv

def read_image(path):
    img = cv.imread(path)
    return img

