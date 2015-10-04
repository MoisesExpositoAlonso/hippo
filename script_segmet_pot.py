from script_image_processing import *
from moi import *

filename='ara.jpg'
filename='araqr.jpg'
filename='P1000363_E3.jpeg'
# filename='~/image/processing_1001/P1000363.jpeg'

# imgb=readgreyimage(filename)
img=readcolimage(filename)


type(img)
height, width, channels = img.shape
print height, width, channels

# ret3,th3 = cv2.threshold(im,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# 
# seg=cv2.threshold(img,cv2.THRESH_OTSU)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)


nameout =filename[:-5] +"_segmented1" +".jpeg"
saveimage(nameout,thresh1)

nameout =filename[:-5] +"_segmented2" +".jpeg"
saveimage(nameout,thresh2)

nameout =filename[:-5] +"_segmented3" +".jpeg"
saveimage(nameout,thresh3)

nameout =filename[:-5] +"_segmented4" +".jpeg"
saveimage(nameout,thresh4)

nameout =filename[:-5] +"_segmented5" +".jpeg"
saveimage(nameout,thresh5)


imgb = cv2.medianBlur(img,5)
 
ret,th1 = cv2.threshold(imgb,127,255,cv2.THRESH_BINARY)
# th2 = cv2.adaptiveThreshold(imgb,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#             cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(imgb,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
 
nameout =filename[:-5] +"_segmented6" +".jpeg"
saveimage(nameout,th1)

nameout =filename[:-5] +"_segmented7" +".jpeg"
saveimage(nameout,th2)

nameout =filename[:-5] +"_segmented8" +".jpeg"
saveimage(nameout,th3)