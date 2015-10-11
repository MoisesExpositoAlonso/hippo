from script_image_processing import *

from moi import *
import sys
import os

# filename=sys.argv[1]
# filename="P1000941_C1.png"
filename='P1000363_E5.jpeg'
# filename='P1000941_C1.jpeg'

# filename=sys.argv[1]

nameroot =filename.split(".")[0]
cwd=os.getcwd()
print cwd
print filename

outname=cwd+nameroot
inname=cwd+filename
print outname
print inname 

print "working over %s" %(filename)



img = readcolimage(filename)
imggrey = readgreyimage(filename)
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hsv=rgb2hsv(img)



print "denoise!"
denoised=denoise(img)
nameout =nameroot +"_denoised" 
saveimage(nameout,denoised)


print "mask hsv !"
maskedhsv=maskhsv(img)
nameout =nameroot +"_maskhsv" 
saveimage(nameout,maskedhsv)

maskedhsv=maskhsv(denoised)
nameout =nameroot +"_denoised_maskhsv" 
saveimage(nameout,maskedhsv)

maskedhsv_denoised=maskhsvdenoise(img)
nameout =nameroot +"_denoised_maskhsv_original" 
saveimage(nameout,maskedhsv)


img=maskedhsv_denoised

ret,thresh0 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

nameout =filename[:-5] +"_segmented0_FINAL" 
saveimage(nameout,thresh1)

nameout =filename[:-5] +"_segmented1_FINAL" 
saveimage(nameout,thresh1)

nameout =filename[:-5] +"_segmented2_FINAL" 
saveimage(nameout,thresh2)

nameout =filename[:-5] +"_segmented3_FINAL" 
saveimage(nameout,thresh3)

nameout =filename[:-5] +"_segmented4_FINAL" 
saveimage(nameout,thresh4)

nameout =filename[:-5] +"_segmented5_FINAL" 
saveimage(nameout,thresh5)


imgb = cv2.medianBlur(rgb2hsv(img)[:,:,2],5)
 
ret,th1 = cv2.threshold(imgb,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(imgb,255,cv2.ADAPTIVE_THRESH_MEAN_C,\

             cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(imgb,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
 
nameout =filename[:-5] +"_segmented6_FINAL" 
saveimage(nameout,th1)

nameout =filename[:-5] +"_segmented7_FINAL" 
saveimage(nameout,th2)

nameout =filename[:-5] +"_segmented8_FINAL" 
saveimage(nameout,th3)
