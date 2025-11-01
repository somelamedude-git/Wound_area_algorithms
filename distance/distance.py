import numpy as np

def calculateArea(standard_distance, area, current_distance):
    # area is in mm^2, we need to convert it to pixels, pixels are tiny squares, im writing so i dont forget
    area_per_pixel = 0.0025
    pixel_side_mm = 0.05
    number_of_pixels = area/area_per_pixel
    distance_units = current_distance/standard_distance

    theta_one = 2* np.arctan(pixel_side_mm/(2*current_distance))
    theta_two = 2* np.arctan(pixel_side_mm/(2*dtandard_distance))

    ratio = theta_two/theta_one
    # one pixel side seems to be ratio amount bigger, ratio can be less than one, or greater than one

    new_side = ratio*pixel_side_mm
    new_area_fake_pixel = new_side*new_side
    number_of_pixels_per_pixel = new_area_fake_pixel/0.0025

    # we have these many pixels in one pixel
    total_pixels = number_of_pixels*number_of_pixels_per_pixel

    area_at_standard = total_pixels*0.0025

    return area_at_standard
