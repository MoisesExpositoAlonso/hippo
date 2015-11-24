from subprocess import *
import sys
import os
import time

infolder=sys.argv[1]
try:
	outfolder=sys.argv[2]
except IndexError:
	outfolder=infolder+"/cropped"
	call(["mkdir",outfolder])


### Find images to analyse

command="find " +infolder+"/"+ "*.JPG > images_to_analyze.txt"
call(command,shell=True, cwd=infolder)
# read list
images_to_analyze=open(infolder+"/"+"images_to_analyze.txt","r")
filesimage=[x.replace("\n","") for x in images_to_analyze]
# remove intermediate file
#command="rm " +infolder+"/"+"images_to_analyze.txt"
#call(command,shell=True)



########################### index of JPG files and qp num #######
## open index 
index=open(infolder+"/"+"index_images.txt","r")
index=[x.replace("\n","").split(",") for x in index]
keys=[x[0].split("/")[-1].split(".")[0] for x in index]
values=[x[2] for x in index]

indexdic={}
for k, v in zip(keys,values):
	indexdic[k]=v

if not indexdic:
	print "Something went wrong, no correct index !!!"
else:
	print "index of images and qp numbers generated"


############################## WORK WITH JPG FILES #############################
### Segment and save image and
# find images to analize
command="find " +infolder+"/"+ "*.JPG > images_to_analyze.txt"
call(command,shell=True, cwd=infolder)
# read list
images_to_analyze=open(infolder+"/"+"images_to_analyze.txt","r")
filesimage=[x.replace("\n","") for x in images_to_analyze]
# remove intermediate file
#command="rm " +infolder+"/"+"images_to_analyze.txt"
#call(command,shell=True)

#print filesimage

### Read the image 

import os
import time

counterlist=0
counter=0
maxparallel=20

for fil in filesimage:
	counterlist=counterlist+1
#	print "------------------------------------------------"
	print "->working over this file",fil
	# print "last modified: %s" % time.ctime(os.path.getmtime(fil))
	# print "created: %s" % time.ctime(os.path.getctime(fil))

# photoname and qpnum
	photoname=fil.split(".")[0].split("/")[-1]
	qpnum=indexdic[photoname]

	newname=outfolder+"/"+photoname+"_qp"+qpnum
# send segmentationm, cropping and count simultaneously

	cmd="python script_crop_tray.py"+" "+fil+ " " + newname
#	print "crop command sent: ", cmd
	p = Popen(cmd, shell=True, stdout=PIPE,stderr=PIPE)


print "sent all crop processes ... "
