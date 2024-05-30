# import cv2

# image=cv2.imread("../Images/image3.png")

# print("Original Image Shape", image.shape)

# # The first parameter is height and the second parameter is width
# img_cropped = image[0:200, 200:500]

# print("Cropped Image Shape", img_cropped.shape)

# cv2.imshow("Original Image", image)

# cv2.imshow("Cropped Image", img_cropped)

# cv2.waitKey(0)


import cv2

img = cv2.imread('./Images/image3.png')

cv2.imshow('img', img)
print('original shape of the image', img.shape)

crop = img[200:600,200:600]

cv2.imshow('crop', crop)
print('original shape of the image', crop.shape)



cv2.waitKey(0)