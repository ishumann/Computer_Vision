'''
scan qr and barcode
'''
#%%
import cv2
import numpy as np
from pyzbar.pyzbar import decode


# image = cv2.imread('./Images/MultipleQR_Bar_code.PNG')
# image = cv2.imread('../../Images/MultipleQR_Bar_code.PNG')
image = cv2.imread('E:\Github\Computer_Vision\Images\MultipleQR_Bar_code.PNG')
#%%
for code in decode(image):
       print(code.data.decode('utf-8'))

#%%
cv2.imshow('input image', image)


cv2.waitKey(0)



# %%
