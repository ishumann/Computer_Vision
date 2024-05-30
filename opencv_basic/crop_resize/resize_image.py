''' test '''


# import cv2

# image=cv2.imread("../Images/lambo.png")

# print("Original Image Shape", image.shape)
# #----> 1000--> resize image width
# #---> 650 __. resize image height
# image_resize=cv2.resize(image, (100, 80))
# print("Resize Image Shape", image_resize.shape)

# cv2.imshow("Original Image", image)

# cv2.imshow("Resize Image", image_resize)

# cv2.waitKey(0)

import cv2

img = cv2.imread('./Images/lambo.png')
# print(int(img.shape[0]*.5), int(img.shape[1],*.5))


test = (int(img.shape[0]*.5), int(img.shape[1]*.5))

resize = cv2.resize(img,test)

print(img.shape,resize.shape)

cv2.imshow('img',img)

cv2.imshow('resize',resize)

cv2.waitKey()
