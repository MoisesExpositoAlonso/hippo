#### PIPELINE FOR IMAGE ANALYSIS OF ARABIDOPSIS ROSETES  ####


### Packages needed to be installed ... in mac easy with brew ... or pip ....

import cv2
import colorsys
from PIL import Image

import matplotlib
import numpy as np
#import scipy
import pylab as P
import matplotlib.pyplot as plt
import os


def readgreyimage(filename):
 im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
 return im


def readcolimage(filename):
 im= cv2.imread(filename,cv2.CV_LOAD_IMAGE_COLOR)
 return im


###########################################################################################


def rgb2hsv(image):
 hsv_img = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
 return (hsv_img)

def rgb2gray(image):
 grayimg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
 return (grayimg)

 # def savehist(histobject,color,filename):
 #    # dictionary = {0:1000, 1:20, 2:15, 3:0, 4:5}
 #    # xmax = max(dictionary.keys())
 #    # ymax = max(dictionary.values())
 #    # # plt.figure() # <- makes a new figure and sets it active (add this)
 #    # plt.hist(dictionary,xmax) # <- finds the current active axes/figure and plots to it
 #    # plt.title(title) 
 #    # plt.xlabel(xlab)
 #    # plt.ylabel(ylab)
 #    # plt.axis([0, xmax, 0, ymax])
 #    plt.plot(histobject, color = color)
	# # plt.xlim([0, 256]) 
 #    # plt.figure() # <- makes new figure and makes it active (remove this)
 #    plt.savefig(filename) # <- saves the currently active figure (which is empty in your code)



############

def denoise(img):
	denoised=cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
	return (denoised)


#######################################################################################

def display(image):
#''' print image into screen untill you press ESC '''
 cv2.imshow('image',image)
 cv2.waitKey(0)



def saveimage(image,name="unknown"):
#''' saves it in the current directory '''
 # directory=os.curdir
 # cv2.imwrite(os.curdir+'/'+name+'.jpeg', image)
 cv2.imwrite(name, image)


def saveimagejpeg(image,name="unknown"):
# #''' saves it in the current directory '''
#  # directory=os.curdir
 cv2.imwrite(name+'.jpeg', image)
 # cv2.imwrite(name, image)


##############################################################################

# def plothist(image):
# 	hist = cv2.calcHist([image],[0],None,[256],[0,256])
# 	#plt.savefig('hist.jpg')
# 	plt.plot(hist)
# 	plt.show()

# def plothisthsv(image):
# 	# hist = cv2.calcHist([image],[0],None,[256],[0,256])
# 	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# 	hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
# 	#plt.savefig('hist.jpg')
# 	plt.plot(hist)
# 	plt.show()

# def savehist(image,filename):
# 	hist = cv2.calcHist([image],[0],None,[256],[0,256])
# 	plt.savefig(filename+'.pdf')
# 	# plt.plot(hist)
# 	# plt.show()


# def savehist2(image,filename):
# 	hist = cv2.calcHist([image],[0],None,[256],[0,256])
# 	fig1 = plt.plot(hist)
# 	plt.show()
# 	plt.draw()
# 	# plt.savefig(filename+'.pdf')
# 	plt.savefig('tessstttyyy.pdf')
# 	# plt.plot(hist)
# 	# plt.show()

# def test(hist,filename):
#     # dictionary = {0:1000, 1:20, 2:15, 3:0, 4:5}
#     xmax = 256
#     ymax = max(hist)
#     plt.figure() # <- makes a new figure and sets it active (add this)
#     plt.hist(hist,xmax) # <- finds the current active axes/figure and plots to it
#     plt.title('Histogram Title') 
#     plt.xlabel('Label')
#     plt.ylabel('Another Label')
#     plt.axis([0, xmax, 0, ymax])
#     # plt.figure() # <- makes new figure and makes it active (remove this)
#     plt.savefig(filename) # <- saves the currently active figure (which is empty in your code)


# def plothisthsv(image):
# 	# hist = cv2.calcHist([image],[0],None,[256],[0,256])
# 	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# 	hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
# 	#plt.savefig('hist.jpg')
# 	plt.plot(hist)
# 	plt.show()

def savehistimg(hist,filename,color="k"):
    # dictionary = {0:1000, 1:20, 2:15, 3:0, 4:5}
   	y=hist.tolist()
	x=list(range(1,257))
	xmax = 256
	ymax = max(y)
	plt.figure() # <- makes a new figure and sets it active (add this)
	# plt.hist(hist,xmax) # <- finds the current active axes/figure and plots to it
	plt.plot(x,y,color)
	plt.title('Image histogram') 
	plt.xlabel('value')
	plt.ylabel('number of pixels')
	# plt.axis([0, xmax, 0, ymax])
	# plt.figure() # <- makes new figure and makes it active (remove this)
	plt.savefig(filename) # <- saves the currently active figure (which is empty in your code)

def savehisthsv(hist,filename,maxval=256,color="k"):
    # dictionary = {0:1000, 1:20, 2:15, 3:0, 4:5}
   	y=hist.tolist()
	x=list(range(1,maxval+1))
	xmax = maxval
	ymax = max(y)
	plt.figure() # <- makes a new figure and sets it active (add this)
	# plt.hist(hist,xmax) # <- finds the current active axes/figure and plots to it
	plt.plot(x,y,color)
	plt.title('Image histogram') 
	plt.xlabel('value')
	plt.ylabel('number of pixels')
	# plt.axis([0, xmax, 0, ymax])
	# plt.figure() # <- makes new figure and makes it active (remove this)
	plt.savefig(filename) # <- saves the currently active figure (which is empty in your code)


#######################################################################################


def splithsvandsave(image):
#'''Split the target image into its red, green and blue channels.
#image - a numpy array of shape (rows, columns, 3).
#output - three numpy arrays of shape (rows, columns) and dtype same as
#   image, containing the corresponding channels. 
#'''
  red = image[:,:,2]
  saveimage('value',red)
  green = image[:,:,1]
  saveimage('saturation',green)
  blue = image[:,:,0]
  saveimage('hue',blue)
  return red, green, blue

def splithsv(image):
#'''Split the target image into its red, green and blue channels.
#image - a numpy array of shape (rows, columns, 3).
#output - three numpy arrays of shape (rows, columns) and dtype same as
#   image, containing the corresponding channels. 
#'''
  value = image[:,:,2]
  saturation = image[:,:,1]
  hue = image[:,:,0]
  return value, saturation, hue


def split_bgr(image):
	b,g,r = cv2.split(image) 
	return b,g,r

def split_bgr_andsave(image,name):
	b,g,r = cv2.split(image) 
	saveimage(name+"blue",b)
	saveimage(name+"green",g)
	saveimage(name+"red",r)
	return b,g,r



# def extractrgb(image):
#  red, green, blue = split_into_rgb_channels(image)
#  for values, color, channel in zip((red, green, blue), ('red', 'green', 'blue'), (2,1,0)):
#  	image = np.zeros((values.shape[0], values.shape[1], 3),  dtype = values.dtype) 
#  	image[:,:,channel] = values
#  return red, green, blue

# def extractrgbandsave(image,name):
#  red, green, blue= split_into_rgb_channels(image)
#  for values, color, channel in zip((red, green, blue), ('red', 'green', 'blue'), (2,1,0)):
# 	 image = np.zeros((values.shape[0], values.shape[1], 3),  dtype = values.dtype) 
# 	 image[:,:,channel] = values
# 	 saveimage('red',red)
# 	 saveimage('green',green)
# 	 saveimage('blue',blue)
#  return red, green, blue


#############################################################################

#def masknongreen(greenimage):
#	# green mask, only pick pixels within this range
#	upper_green = np.array([128,185,20]) 
#	lower_green = np.array([42,97,0]) 
#	mask = cv2.inRange(image, lower_green,upper_green)
#	# then bitwise and mask original image 
#	result = cv2.bitwise_and(image,image, mask= mask)
#	return(result)


###@@@@ ON PROGRESS @@@@####

def maskhsv(img):
	
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


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
	# result = cv2.bitwise_and(result,result, mask= v_mask)
	return(result)

def maskhsvdenoise(img):
	
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
	result = cv2.bitwise_and(result,result, mask= v_mask)
	return(result)


def mask1into2(mask, onechannelimg):
	result = cv2.bitwise_and(onechannelimg,onechannelimg, mask= mask)
	return(result)	

def greenminusblueandintermediate(image):
	imgdif=image[1]-image[0]
	upper = 170
	lower = 60
	print imgdif
	mask = cv2.inRange(imgdif, lower,upper)
	# then bitwise and mask original image 
	result = cv2.bitwise_and(image[1],image[1], mask= mask)
	return(result)	

def greenminusblueandintermediateoriginal(image,img):
	imgdif=image[1]-image[0]
	upper = 170 
	lower = 60
	print imgdif
	mask = cv2.inRange(imgdif, lower,upper)
	# then bitwise and mask original image 
	result = cv2.bitwise_and(img,img, mask= mask)
	return(result)	


def maskgreen(image):
	# green mask, only pick pixels within this range, using only chanel green image
	upper_green = 185 
	lower_green = 97
	mask = cv2.inRange(image, lower_green,upper_green)
	# then bitwise and mask original image 
	result = cv2.bitwise_and(image,image, mask= mask)
	return(result)
#	return(mask)

def maskgreen(image):
	# green mask, only pick pixels within this range, using only chanel green image
	upper_green = 255 
	lower_green = 97
	mask = cv2.inRange(image, lower_green,upper_green)
	# then bitwise and mask original image 
	result = cv2.bitwise_and(image,image, mask= mask)
	return(result)
#	return(mask)


def maskblue(image):
	# blue mask, only pick pixels within this range, using only chanel blue image
	upper_blue = 218
	lower_blue = 130
	mask = cv2.inRange(image, lower_blue,upper_blue)
	# then bitwise and mask original image 
#	mask_inverse=cv2.bitwise_not(mask)
	result = cv2.bitwise_and(image,image, mask= mask)  ## notice that blue is not wanted!
	return(result)

###### crop 

def crop (image, x1,x2,y1,y2):
	crop_img = image[y1:y2,x1:x2]
	return(crop_img)



#################################################################

###### generate index of positions for cropping



######### END FUNCTIONS ########

######### TO REFINE ########

# # add two images
# cv2.add()

# cv2.absdiff
# cv2.subtract




# #ret,thinv = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)

# ret,th = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
# #ret,th2 = cv2.threshold(th,100,220,cv2.THRESH_BINARY)
# #splitrgbandsave(th)
# saveimage('binarythreshold',th)

# #medianth = cv2.medianBlur(th,5)
# medianth = cv2.medianBlur(th,7)
# saveimage('binarythreshold_medianblur',medianth)

# newrgb=splitrgb(medianth)
# splitrgbandsave(medianth)

# #newrgb

# difference=newrgb[1]-newrgb[0]
# saveimage('binarythreshold_medianblur_greenblue',difference)

# maskblueingreen=cv2.bitwise_and(newrgb[1],newrgb[1], mask= newrgb[0])
# saveimage('binarythreshold_medianblur_maskblueingreen',maskblueingreen)

# #median = cv2.medianBlur(difference,5)
# #saveimage('greenblue_blurmedian_afterthreshold',difference)

# #difference=newrgb[1]-newrgb[0]
# #median2 = cv2.medianBlur(difference,5)
# #saveimage('greenblue_blurmedian_afterthreshold_blurmedian',difference)

# median2gaus = cv2.GaussianBlur(difference,(5,5),0)
# saveimage('greenblue_blurmedian_afterthreshold_blurgauss',difference)



# extractoriginal = cv2.bitwise_and(image,image, mask= median2)
# saveimage('aftersegmentation_extract',extractoriginal)


# #ret3,th3 = cv2.threshold(difference,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# #saveimage('greenblue_afterthreshold_otsugauss',th3)

# #def combinedmaskgb(image):
# #	upper_blue = 20
# #	lower_blue = 0
# #	maskblue = cv2.inRange(image, lower_blue,upper_blue)
# #	upper_green = 185 
# #	lower_green = 97
# #	maskgreen = cv2.inRange(image, lower_green,upper_green)



# #def maskblue(image):
# #	# green mask, only pick pixels within this range
# #	upper_green = np.array([128,185,20]) 
# #	lower_green = np.array([42,97,0]) 
# #	mask = cv2.inRange(image, lower_green,upper_green)
# #	# then bitwise and mask original image 
# #	result = cv2.bitwise_and(image,image, mask= mask)
# #	return(result)





