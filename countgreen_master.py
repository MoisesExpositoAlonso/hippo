
from module_image_processing import *

from moi import *
import sys
import os
from subprocess import *


############################## FOLDER TO WORK #############################

outfolder="/Users/moisesexpositoalonso/image1001g/tmp"
call("mkdir cropped",shell=True,cwd=outfolder)
outfolder_cropped="/Users/moisesexpositoalonso/image1001g/tmp/cropped"
infolder="/Users/moisesexpositoalonso/image1001g"

# outfolder="/ebio/abt6_projects9/ath_1001G_image_pheno/tmp"
# call("mkdir cropped",shell=True,cwd=outfolder)
# outfolder_cropped="/ebio/abt6_projects9/ath_1001G_image_pheno/tmp/cropped"
# infolder="/ebio/abt6_projects9/ath_1001G_image_pheno/scripts"


# outfolder=sys.argv[1]
# outfolder_cropped=sys.argv[1]

# infolder=sys.argv[2]

# tmpfolder=outfolder+"/segmented/"

# tmpfoldercount=outfolder+"/segmented_cropped/"

# removeyesno=sys.argv[1]

workingfolder=os.getcwd()

############################## WORK WITH JPG FILES #############################
### Segment and save image and
# find images to analize
command="find " +infolder+"/"+ "*.JPG > images_to_analyze.txt"
call(command,shell=True)
# read list
images_to_analyze=open(infolder+"/"+"images_to_analyze.txt","r")
filesimage=[x.replace("\n","") for x in images_to_analyze]
# remove intermediate file
command="rm " +infolder+"/"+"images_to_analyze.txt"
call(command,shell=True)
#print filesimage

### Read the image 

import os
import time

counter=0
maxparallel=1

for fil in filesimage:
	print "------------------------------------------------"
	print "->working over this file",fil
	# print "last modified: %s" % time.ctime(os.path.getmtime(fil))
	# print "created: %s" % time.ctime(os.path.getctime(fil))

# send segmentationm, cropping and count simultaneously

	cmd="time python countgreen_child.py"+ " " + fil + " " +outfolder_cropped
#	print "crop command sent: ", cmd
	p = Popen(cmd, shell=True)

	counter=counter+1
	print counter
	if counter == maxparallel:
		p.wait()
		counter=0
	else:
		pass

# out of loop


