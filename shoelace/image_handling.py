import cv2 as cv

def read_image(path):
    img = cv.imread(path)
    return img

def rescale_image(frame, scale):
    width = int (frame[1]*scale)
    height = int(frame[0]*scale)

def make_grayscale(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    return gray

def make_blur(frame, kernel_size):
    blur = cv.GaussianBlur(frame, (kernel_size, kernel_size), cv.BORDER_DEFAULT)
    dimensions = (width,height)
    return cv.rescale(frame, dimensions, interpolation=cv.INTER_AREA)

