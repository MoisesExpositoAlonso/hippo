from script_image_processing import *

from moi import *
import sys
import os

# filename=sys.argv[1]
# filename="P1000941_C1.png"
filename='P1000363_E5.jpeg'
filename='P1000941_C1.jpeg'

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




channel = cv2.split(img)
channelnum=(0,1,2)
color = ('b','g','r')

for chan in zip(channelnum, color):
	print chan
	print "this is channel num: %s" %(chan[0])
	print "this is the color: %s" %(chan[1])
	# hist = cv2.calcHist(channel[chan[0]],[0], None, [256], [0, 256])
	hist = cv2.calcHist(channel,[chan[0]], None, [256], [0, 256])
	
	# features.extend(hist)
	print hist
	nameout =nameroot +"_hist_"+chan[1]
	print nameout
	savehistimg(hist,nameout+".pdf",color=chan[1])




# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# savehistimg(hist,nameout+".pdf",color=chan[1])

hsv=rgb2hsv(img)

channelnum=(0,1,2)
hsvcolor = ('h','s','v')
maxhsv=(180,256,256)
for chan in zip(channelnum, hsvcolor,maxhsv):
	print chan
	print hsv[chan[0]]
	# print "this is channel num: %s" %(chan[0])
	# print "this is the color: %s" %(chan[1])
	hist = cv2.calcHist(hsv[:,:,chan[0]],[0], None, [256], [0, 256])
	print hist
	# hist = cv2.calcHist(hsv[chan[0]],[0], None, [256], [0, 256])
	# features.extend(hist)
	# print hist
	nameout =nameroot +"_hist_"+chan[1]
	savehisthsv(hist,nameout+".pdf",maxval=256)
	saveimage(image=hsv[:,:,chan[0]],name=str( nameroot +"_" + chan[1]) )
	print str( nameroot +"_" + chan[1]) 





## 70 to 140 is all kind of greens

###############################################################
# channels = [0,1] # because we need to process both H and S plane.
# bins = [180,256] # 180 for H plane and 256 for S plane
# range = [0,180,0,256] # Hue value lies between 0 and 180 Saturation lies between 0 and 256

# hist = cv2.calcHist( hsv, 0, 1, None, 180, 256, 0, 180, 0, 256 )

# plt.imshow(hist)
# plt.show(block=False)	