from script_image_processing import *
from moi import *
import sys

# filename='ara.jpg'
# filename='araqr.jpg'
# filename='P1000363_E3.jpeg'
# # filename='P1000363_E6.jpeg'
# filename='P1000363.jpg'
# filename="P1000941.jpg"
filename=sys.argv[1]

print "working over %s" %(filename)


# imgb=readgreyimage(filename)
img=readcolimage(filename)




type(img)
height, width, channels = img.shape
print height, width, channels


imghsv=rgb2hsv(img)
splithsvandsave(imghsv)
saveimage(filename[:-5] +"_hsv_h"  , imghsv[0] )
saveimage(filename[:-5] +"_hsv_s"  , imghsv[1] )
saveimage(filename[:-5] +"_hsv_v"  , imghsv[2] )


denoised=denoise(img)
nameout =filename[:-5] +"_denoised" 
saveimage(nameout,denoised)


# ret3,th3 = cv2.threshold(im,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# 
# seg=cv2.threshold(img,cv2.THRESH_OTSU)
ret,thresh0 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

nameout =filename[:-5] +"_segmented0" 
saveimage(nameout,thresh1)

nameout =filename[:-5] +"_segmented1" 
saveimage(nameout,thresh1)

nameout =filename[:-5] +"_segmented2" 
saveimage(nameout,thresh2)

nameout =filename[:-5] +"_segmented3" 
saveimage(nameout,thresh3)

nameout =filename[:-5] +"_segmented4" 
saveimage(nameout,thresh4)

nameout =filename[:-5] +"_segmented5" 
saveimage(nameout,thresh5)



## other morphology transformation
kernel = np.ones((5,5),np.uint8)


closing = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
nameout =filename[:-5] +"_closing" 
saveimage(nameout,closing)

opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
nameout =filename[:-5] +"_open" 
saveimage(nameout,opening)

dilation = cv2.dilate(thresh1,kernel,iterations = 1)
nameout =filename[:-5] +"_dilution"
saveimage(nameout,dilation)


# http://stackoverflow.com/questions/27014207/failure-to-use-adaptivethreshold

imgb=readgreyimage(filename)

imgb = cv2.medianBlur(imgb,5)
 
ret,th1 = cv2.threshold(imgb,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(imgb,255,cv2.ADAPTIVE_THRESH_MEAN_C,\

             cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(imgb,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
 
nameout =filename[:-5] +"_segmented6" 
saveimage(nameout,th1)

nameout =filename[:-5] +"_segmented7" 
saveimage(nameout,th2)

nameout =filename[:-5] +"_segmented8" 
saveimage(nameout,th3)




###### connected different 

ret,binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

separate=splithsv(binary)

bin_edge = cv2.adaptiveThreshold(separate[1],255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
nameout =filename[:-5] +"_binary_shape" 
saveimage(nameout,bin_edge)


##### green only
# separate colors

imgsplit=split_bgr_andsave(img,filename[:-5])
type(img)
type(imgsplit)
# nameout =filename[:-5] +"_imagesplitted" 
# saveimage(nameout,imgsplit)

# geen mask, identify stuff
green=maskgreen(imgsplit[1])
nameout =filename[:-5] +"_maskedgreen" 
saveimage(nameout,green)

# difference with high green and low blue
greenminusblue=imgsplit[1]-imgsplit[0]
nameout =filename[:-5] +"_green_minus_blue" 
saveimage(nameout,greenminusblue)

# difference and mask
grenminusbluemask=greenminusblueandintermediate(imgsplit)
nameout =filename[:-5] +"_green_minus_blue_&mask" 
saveimage(nameout,grenminusbluemask)

grenminusbluemask=greenminusblueandintermediateoriginal(imgsplit,img)
nameout =filename[:-5] +"_green_minus_blue_&mask_intooriginal" 
saveimage(nameout,grenminusbluemask)

### over the blue mask do several more

kernel = np.ones((5,5),np.uint8)
# kernel = np.ones((8,8),np.uint8)


grenminusbluemask

grenminusbluemask_noise5 = cv2.medianBlur(grenminusbluemask,5)
nameout =filename[:-5] +"_green_minus_blue_noise5" 
saveimage(nameout,grenminusbluemask_noise5)

grenminusbluemask_noise7 = cv2.medianBlur(grenminusbluemask,7)
nameout =filename[:-5] +"_green_minus_blue_noise7" 
saveimage(nameout,grenminusbluemask_noise7)

grenminusbluemask_noise9 = cv2.medianBlur(grenminusbluemask,9)
nameout =filename[:-5] +"_green_minus_blue_noise9" 
saveimage(nameout,grenminusbluemask_noise9)

closing_gb = cv2.morphologyEx(grenminusbluemask, cv2.MORPH_CLOSE, kernel)
nameout =filename[:-5] +"_greenminusbluemaks_closing" 
saveimage(nameout,closing_gb)

opening_gb = cv2.morphologyEx(grenminusbluemask, cv2.MORPH_OPEN, kernel)
nameout =filename[:-5] +"_greenminusbluemaks_open" 
saveimage(nameout,opening_gb)

dilation_gb = cv2.dilate(grenminusbluemask,kernel,iterations = 3)
nameout =filename[:-5] +"_greenminusbluemaks_dilute"
saveimage(nameout,dilation_gb)

erode_gb = cv2.erode(grenminusbluemask,kernel,iterations = 1)
nameout =filename[:-5] +"_greenminusbluemaks_erode"
saveimage(nameout,erode_gb)

erode_close_gb = cv2.morphologyEx(erode_gb, cv2.MORPH_CLOSE, kernel)
nameout =filename[:-5] +"_greenminusbluemaks_erode_close"
saveimage(nameout,erode_close_gb)

erode_close_gb_gaus = cv2.GaussianBlur(erode_close_gb,(5,5),0)
nameout =filename[:-5] +"_greenminusbluemaks_erode_close_blur"
saveimage(nameout,erode_close_gb_gaus)

grenminusbluemask_edges = cv2.adaptiveThreshold(split_bgr(grenminusbluemask)[1],255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
nameout =filename[:-5] +"_green_minus_blue_&mask_edges" 
saveimage(nameout,grenminusbluemask_edges)

grenminusbluemask_canny = cv2.Canny(split_bgr(grenminusbluemask)[1],100,200)
nameout =filename[:-5] +"_green_minus_blue_&mask_canny" 
saveimage(nameout,grenminusbluemask_canny)


# greenminusbluemaksnoise9_dilute = cv2.dilate(grenminusbluemask_noise9,kernel,iterations = 1)
# nameout =filename[:-5] +"_greenminusbluemaksnoise9_dilute"
# saveimage(nameout,greenminusbluemaksnoise9_dilute)

# ret,greenminusbluemaksnoise9_dilute_threshold= cv2.inRange(greenminusbluemaksnoise9_dilute[1],60,100)
# nameout =filename[:-5] +"_greenminusbluemaksnoise9_dilute_rangemask"
# saveimage(nameout,greenminusbluemaksnoise9_dilute_threshold)


# print type (grenminusbluemask_canny	)
# print grenminusbluemask_canny
# print type (grenminusbluemask)
# print grenminusbluemask

# greenminusblue_plus_edges=cv2.add(grenminusbluemask_canny,grenminusbluemask)
# nameout =filename[:-5] +"_green_minus_blue_addedges" 
# saveimage(nameout,greenminusblue_plus_edges)


# maskblur_greenminusblue= mask1into2 (greenminusbluemaksnoise9_dilute_threshold,split_bgr(grenminusbluemask)[1])
# nameout =filename[:-5] +"_green_minus_blue_&maskblur" 
# saveimage(nameout,maskblur_greenminusblue)


# grenminusbluemask
# grenminusbluemask_median = cv2.medianBlur(grenminusbluemask,9)

# grenminusbluemask_maskmedian = cv2.bitwise_and(grenminusbluemask,grenminusbluemask, mask= grenminusbluemask_median[1])
# # saveimage('aftersegmentation_extract',extractoriginal)
# nameout =filename[:-5] +"grenminusbluemask_maskmedian" 
# saveimage(nameout,grenminusbluemask_maskmedian)


