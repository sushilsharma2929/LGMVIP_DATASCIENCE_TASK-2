
# Data Science Internship @LetsGrowMore.

# Name : Sushil Sharma

# Task 1 :-Image To Pencil Sketch with Python.

# Step 1 :- Import librery.

from google.colab.patches import cv2_imshow
import cv2

# Step 2 :- Read the Image.

Hitmanimage = cv2.imread('Rohit.jpg', 1)
cv2_imshow(Hitmanimage)

# Step 3 :-Convert Image into Grayscale

gray_image_of_Hitman=cv2.cvtColor(Hitmanimage, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray_image_of_Hitman)

# Step 4 :-Invert the gray scale Image

inverted_gray_image_of_Hitman=255-gray_image_of_Hitman
cv2_imshow(inverted_gray_image_of_Hitman)

# Step 5 :-Blur the image by gaussian Function

blurred_img_of_Hitman = cv2.GaussianBlur(inverted_gray_image_of_Hitman, (21,21), 0)
cv2_imshow(blurred_img_of_Hitman)

# Step :-6 Invert the blurred image.


inverted_blurred_image_of_Hitman = 255-blurred_img_of_Hitman
cv2_imshow(inverted_blurred_image_of_Hitman)

# Step :- 7 Create the pencil sketch image.

pencil_sketch_image_of_Hitman = cv2.divide(gray_image_of_Hitman,inverted_blurred_image_of_Hitman,scale=256.0)
cv2_imshow(pencil_sketch_image_of_Hitman)
