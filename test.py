import cv2
import numpy as np


# Read in the image
image = cv2.imread("tested.jpg")

# Split the image into two halves
height, width, _ = image.shape
left_half = image[:, :480]
right_half = image[:, 480:]

# Count the number of white pixels in each half
left_half_white_pixels = 0
right_half_white_pixels = 0

for row in left_half:
    for pixel in row:
        if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
            left_half_white_pixels += 1

for row in right_half:
    for pixel in row:
        if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
            right_half_white_pixels += 1

# Print the results
print("Number of white pixels in left half:", left_half_white_pixels)
print("Number of white pixels in right half:", right_half_white_pixels)











