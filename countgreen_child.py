## PIPELINE CHUNK FOR SEGMENTATION AND CROPPING OF TRAYS  ####


from moi import *
from module_image_processing import *
import time
import os
import sys

# 1 ## Read image

fil=sys.argv[1]
# example
# fil="/Users/moisesexpositoalonso/image1001g/P1000363.JPG"
#fil="/Users/moisesexpositoalonso/image1001g/P1000544.JPG"
outfolder=sys.argv[2]



photoname=fil.split(".")[0].split("/")[-1]

# 2 ## File info
(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(fil)
#print "last modified: %s" % time.ctime(mtime)
mytime=time.ctime(mtime)
mytime=mytime.replace("  "," ").split(" ")
timestring="2015"+"-"+mytime[1]+"-"+mytime[2]
#print timestring

#mytime=time.ctime(os.path.getctime(fil))
#mytime=mytime.split(" ")
#listposition=[1,2,4]
#listposition=[1,2,4]
#finaltime=[x[1] for x in enumerate(mytime) if x[0] in listposition]
#timestring=finaltime[2]+"-"+finaltime[0]+"-"+finaltime[1]
#timestring=mytime[5]+"-"+mytime[1]+"-"+mytime[3]
#timestring="2015"+"-"+mytime[1]+"-"+mytime[2]
#print timestring


# 3 ## Segment

img = readcolimage(fil)

maskedhsv_denoised=maskhsvdenoise(img)
im=maskedhsv_denoised
#print "segmented image: ", fil
saveimagejpeg(image=im, name=outfolder+"/segmented/"+photoname+"_green")


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

csvname=outfolder+"/results/"+timestring+"_"+photoname+"_results_greencount.csv"
print csvname

outcount=open(csvname,"w")
listoutcount=[]


for r in rows:
  for c in columns:
    # if str(r)+str(c) any 
    # print str(r)+str(c)
    # nameout =newname +"_" +str(r)+str(c)
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
        # crop the pot
        cropim=crop(im,x1=x1,x2=x2,y1=y1,y2=y2)
        # grey transform
        cropim_grey=rgb2grey(cropim)
        # count green pixels
        count=cv2.countNonZero(cropim_grey) 
        # produce the data line
        traypos=str(r)+str(c)
        towrite=[str(timestring),str(photoname),str(traypos),str(count)]
        listoutcount.append(towrite)

#print listoutcount

if not listoutcount:
  print "Something went wrong, listoutcount is empty !!!"

for line in listoutcount:
    outcount.write(str(','.join(line)+"\n"))

outcount.close()

print "csv written"
print "Finished child process ..."
