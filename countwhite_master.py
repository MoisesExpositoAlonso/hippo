
from module_image_processing import *

from moi import *
import datetime
import time
import sys
import os
from subprocess import *


now1=time.strftime("%d-%b-%Y %H:%M:%S")
print "time start process: ", now1

############################## FOLDER TO WORK #############################


#outfolder="/Users/moisesexpositoalonso/image1001g/tmp"
#call("mkdir cropped",shell=True,cwd=outfolder)
#outfolder_cropped="/Users/moisesexpositoalonso/image1001g/tmp/cropped"
#infolder="/Users/moisesexpositoalonso/image1001g"

# outfolder="/ebio/abt6_projects9/ath_1001G_image_pheno/tmp"
# outfolder_cropped="/ebio/abt6_projects9/ath_1001G_image_pheno/tmp/cropped"
# infolder="/ebio/abt6_projects9/ath_1001G_image_pheno/data/greenhouse_drought_experiment/alljpg"
#infolder="/ebio/abt6_projects9/ath_1001G_image_pheno/toy"


# outfolder_cropped=sys.argv[1]

infolder=sys.argv[1]
try:
	outfolder=sys.argv[2]
except IndexError:
	outfolder=infolder

### Create output files

call("mkdir segmented_white",shell=True,cwd=outfolder)
call("mkdir results_white",shell=True,cwd=outfolder)


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


# send segmentationm, cropping and count simultaneously

	cmd="python countwhite_child.py"+" "+qpnum + " " + fil + " " +outfolder
#	print "crop command sent: ", cmd
	p = Popen(cmd, shell=True, stdout=PIPE,stderr=PIPE)

# check for errors. problem is that you have to wait until it finishes .. so no parallel
	out, err = p.communicate()	
	if err:
		print "standard error of subprocess:"
		print err

# set a limit to the paralelisation
	counter=counter+1
	print counter
	
	if counter == maxparallel:
		p.wait()
		counter=0
	else:
		pass
# wait in the last file iteration.
	if counterlist == len(filesimage):
		p.wait()
	else:
		pass
# out of loop

########################################################
## Put together all spreadsheets.

command="find " +outfolder+"/results_white/"+ "*.csv > spreadsheets_to_analyze.txt"
call(command,shell=True, cwd=outfolder+"/results")
spreadsheets=open(outfolder+"/results_white/"+"spreadsheets_to_analyze.txt","r")
spreadsheets=[x.replace("\n","") for x in spreadsheets]


## read each file and append to the bit csv
bigcsv=["date,image,position,green,qppot\n"]

for csv in spreadsheets:
	csvread=open(csv,"r")
	csvread=[x for x in csvread]
	for row in csvread:
		bigcsv.append(row)
	# csvread=[x.replace("\n","").split(",") for x in csvread]
	# print csvread
	# keyname=csvread[0][1]
	# valuename=indexdic[keyname]
	# for row in csvread:
	# csvread[0].append(valuename)

csvname=outfolder+"/results_white/"+"bigcsv_results_greencount.csv"
outbigcsv=open(csvname,"w")
for line in bigcsv:
	outbigcsv.write(line)
outbigcsv.close()

########################################################
# finish time
now2=time.strftime("%d-%b-%Y %H:%M:%S")

print "Finished master process at time ", now2

d1 = datetime.datetime.strptime(now1, '%d-%b-%Y %H:%M:%S')
d2 = datetime.datetime.strptime(now2, '%d-%b-%Y %H:%M:%S')

difftime = (d2 - d1).total_seconds() / 60
print "Total time of the analysis: ", difftime, " minutes"
