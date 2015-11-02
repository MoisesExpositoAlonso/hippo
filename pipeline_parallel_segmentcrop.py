## PIPELINE CHUNK FOR SEGMENTATION AND CROPPING OF TRAYS  ####



from module_image_processing import *
from moi import *
import sys

# 1 ## Read image

fil=sys.argv[1]

newname=sys.argv[2]

#im=readcolimage(filename)
# type(im)
# height, width, channels = im.shape
# print height, width, channels


# 2 ## Segment

img = readcolimage(fil)

maskedhsv_denoised=maskhsvdenoise(img)
im=maskedhsv_denoised
#print "segmented image: ", fil

#nameout =outname +"_segmented"
#cv2.imwrite(nameout+".jpeg",maskedhsv_denoised)
#print "saved image ",nameout+".jpeg"
#saveimage(name=nameout,image=maskedhsv_denoised)

# maskedhsv_denoised_binary = cv2.medianBlur(rgb2hsv(maskedhsv_denoised)[:,:,2],5) 
# ret,th1 = cv2.threshold(maskedhsv_denoised_binary,127,255,cv2.THRESH_BINARY) ### SO FIRST THE NORMAL, THEN I CAN TRY THIS



# 3 ## get the index of pot positions

fileindex="index_pots_pertray.tsv"
# print fileindex
# indexpots=open(fileindex,"r")
# indexpots=[x.replace("\n","").split("\t") for x in indexpots]
# print indexpots

table=readtabtable(filename=fileindex)
# print table


rows= ["A", "B",  "C",  "D", "E"] 
columns=[1,2,3,4,5,6,7,8]

# 3 ## crop and save

for r in rows:
 for c in columns:
  # if str(r)+str(c) any 
  # print str(r)+str(c)
  nameout =newname +"_" +str(r)+str(c)
  for t in table:
   if "row" in t:
    continue
   if str(t[0]) == r and float (t[1]) ==float(c):
    # print t[2:6]
    # x1= int(t[2]) -20
    # x2= int(t[3]) +20
    # y1= int(t[4]) -20
    # y2= int(t[5]) +20
    x1= int(t[2]) 
    x2= int(t[3]) 
    y1= int(t[4]) 
    y2= int(t[5]) 
    # print [x1,x2,y1,y2]
    cropim=crop(im,x1=x1,x2=x2,y1=y1,y2=y2)
    # print nameout
    saveimage(name=nameout+".jpeg",image=cropim) 
