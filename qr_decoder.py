from qrtools import QR
from moi import *
from script_image_processing import *
import sys


# get the picture file name and root name
mypicture=sys.argv[1]
nameroot =mypicture.split(".")[0]

# read the picture only in grey values
imggrey = readgreyimage(mypicture)

# crop it to the top-left corner
x1=220
x2=725	
y1=597	
y2=1050

cropim=crop(imggrey,x1=x1,x2=x2,y1=y1,y2=y2)

# threshold it and save
imgb=cropim
ret,th1 = cv2.threshold(imgb,127,255,cv2.THRESH_BINARY) 
nameout =nameroot+"_grey_threshold" 
saveimagejpeg(name=nameout,image=th1)

# decode it
myCode = QR(filename=mypicture)
if myCode.decode():
  #print myCode.data
  #print myCode.data_type
  print myCode.data_to_string()
