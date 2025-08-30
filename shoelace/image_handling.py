import cv2 as cv
import numpy as np

def shoelace_formula(boundary_points, absoluteValue=True):
    points = np.array(boundary_points)
    x = points[:, 0]
    y = points[:, 1]

    area = 0.5 * np.sum(x * np.roll(y, -1) - y * np.roll(x, -1))

    return abs(area) if absoluteValue else area

def read_image(path):
    img = cv.imread(path)
    return img

def rescale_image(frame, scale): #Will integrate when needed
    width = int (frame[1]*scale)
    height = int(frame[0]*scale)

def make_grayscale(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    return gray

def make_blur(frame, kernel_size=3):
    blurred = cv.GaussianBlur(frame, (3,3), 0)
    return blurred

def binarize_image(frame):
    _, imageThres = cv.threshold(frame, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    return imageThres

def canny_image(thresholdFrame):
    canny_img = cv.Canny(thresholdFrame, 0, 0)
    return canny_img

def get_contours(cannyImage):
    contours, _ = cv.findContours(cannyImage, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    return contours

def filter_contours(contours):
    max_area = max(cv.contourArea(c) for c in contours)
    min_area = 0.0*max_area
    max_coverage = 0.95*max_area
    filtered = [c for c in contours if cv.contourArea(c)>min_area and cv.contourArea(c)<max_coverage]
    return filtered

def combine_and_order_points(filtered_points):
    all_points = np.vstack(filtered_points)
    all_points = all_points[:, 0, :]
    unique_points = np.unique(all_points, axis=0)
    hull = cv.convexHull(unique_points)
    hull = hull[:,0,:]
    return hull

def find_area(frame):
    gray_ = make_grayscale(frame)
    blur_ = make_blur(gray_)
    binary_ = binarize_image(blur_)
    canny_ = canny_image(binary_)
    contours = get_contours(canny_)
    filtered = filter_contours(contours)
    points = combine_and_order_points(filtered)

    area = shoelace_formula(points)
    return area*0.04

def final_(path):
    img = read_image(path)
    area = find_area(img)
    return area
