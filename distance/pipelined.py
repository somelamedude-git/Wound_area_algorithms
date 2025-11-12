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
    return area

def final_(path):
    img = read_image(path)
    area = find_area(img)
    return area

import numpy as np


def calc_PPI(width_pixels, height_pixels, diagonal_in_inches):
    diagonal_in_pixels = np.sqrt((width_pixels**2)+(height_pixels**2))
    return diagonal_in_pixels/diagonal_in_inches

def calculateArea(standard_distance, area, current_distance, PPI):
    # area is in mm^2, we need to convert it to pixels, pixels are tiny squares, im writing so i dont forget
    area_per_pixel = (25.4/PPI)**2
    pixel_side_mm = (25.4/PPI)
    number_of_pixels = area
    distance_units = current_distance/standard_distance

    theta_one = 2* np.arctan(pixel_side_mm/(2*current_distance))
    theta_two = 2* np.arctan(pixel_side_mm/(2*standard_distance))

    ratio = theta_two/theta_one
    # one pixel side seems to be ratio amount bigger, ratio can be less than one, or greater than one

    new_side = ratio*pixel_side_mm
    new_area_fake_pixel = new_side*new_side
    number_of_pixels_per_pixel = new_area_fake_pixel/area_per_pixel

    # we have these many pixels in one pixel
    total_pixels = number_of_pixels*number_of_pixels_per_pixel

    area_at_standard = total_pixels*area_per_pixel

    return area_at_standard

def final_final(path, width_pixels, height_pixels, diagonal_in_inches, current_distance, standard_distance=100):
    ppi = calc_PPI(width_pixels, height_pixels, diagonal_in_inches)
    area = final_(path)
    standard_area = calculateArea(standard_distance, area, current_distance, ppi)

    return standard_area

