from script_image_processing import *

from moi import *
import sys
import os


# filename=sys.argv[1]
filename="/Users/moisesexpositoalonso/image1001g/tmp/2015-Oct-5_P1000363_A1.jpeg"

nameroot =filename.split(".")[0]


img = readcolimage(filename)

maskedhsv_denoised=maskhsvdenoise(img)
nameout =nameroot +"_segmented" 
saveimage(nameout,maskedhsv_denoised)

imgb = cv2.medianBlur(rgb2hsv(img)[:,:,2],5) 
ret,th1 = cv2.threshold(imgb,127,255,cv2.THRESH_BINARY) 
nameout =filename[:-5] +"_segmented_binary" 
saveimage(nameout,th1)




denoised=denoise(img)
hsv = rgb2hsv(denoised)

h_upper=70
h_lower=30

s_upper=255
s_lower=65

v_upper=220
v_lower=20


hue=hsv[:,:,0]
saturation=hsv[:,:,1]
value=hsv[:,:,2]

h_mask = cv2.inRange(hue, h_lower,h_upper)
s_mask = cv2.inRange(saturation, s_lower,s_upper)
v_mask = cv2.inRange(value, v_lower,v_upper)

result = cv2.bitwise_and(img,img, mask= h_mask)
result = cv2.bitwise_and(result,result, mask= s_mask)
