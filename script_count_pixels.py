from script_image_processing import *
from moi import *

filename='P1000363_E3_green_minus_blue_&mask_intooriginal.jpeg'
filename='P1000363_E3_green_minus_blue_&mask.jpeg'
filename="P1000363_E5_denoised_maskhsv_original.jpeg"

filename="P1000363_E5_segmented6_FINAL.JPEG"

img=readgreyimage(filename)

fileoutputname="count_pixels_"+filename[0:11]+".txt"
fileoutput=open(fileoutputname, "w")

count=cv2.countNonZero(img) 
print "this is the number of nonzero pixels : %s" %(count)

fileoutput.write(filename[0:11]+"\t"+str(count) )