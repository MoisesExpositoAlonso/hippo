
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

removeyesno=sys.argv[1]

workingfolder=os.getcwd()

############################## WORK WITH JPG FILES #############################
### Segment and save image and

command="find " +infolder+"/"+ "*.JPG > images_to_analyze.txt"
call(command,shell=True)

images_to_analyze=open(infolder+"/"+"images_to_analyze.txt","r")
filesimage=[x.replace("\n","") for x in images_to_analyze]
#print filesimage

### Read the image 

import os
import time

counter=0

for fil in filesimage:
	print "------------------------------------------------"
	print "->working over this file",fil
	# print "last modified: %s" % time.ctime(os.path.getmtime(fil))
	# print "created: %s" % time.ctime(os.path.getctime(fil))

	mytime=time.ctime(os.path.getctime(fil))
	mytime=mytime.split(" ")
	listposition=[1,2,4]
	finaltime=[x[1] for x in enumerate(mytime) if x[0] in listposition]
	timestring=finaltime[2]+"-"+finaltime[0]+"-"+finaltime[1]
#	print timestring

### Create the new name including root of picture date of creation

	nameroot =fil.split("/")[-1].split(".")[0]
	print "this is nameroot ",nameroot
	newroot=timestring+"_"+nameroot
	outname=outfolder+"/"+newroot 
	# print newroot # example 2015_Oct_5_P1000363_A4.jpeg
#	print "this is outname",outname
	
### segment before cropping	
### send a job of cropping

	#img = readcolimage(fil)

	#maskedhsv_denoised=maskhsvdenoise(img)
	#nameout =outname +"_segmented" 
	#cv2.imwrite(nameout+".jpeg",maskedhsv_denoised)
	#print "saved image ",nameout+".jpeg"
	#saveimage(name=nameout,image=maskedhsv_denoised)

	# maskedhsv_denoised_binary = cv2.medianBlur(rgb2hsv(maskedhsv_denoised)[:,:,2],5) 
	# ret,th1 = cv2.threshold(maskedhsv_denoised_binary,127,255,cv2.THRESH_BINARY) ### SO FIRST THE NORMAL, THEN I CAN TRY THIS

# send segmentation and cropping simultaneously

	cmd="python pipeline_parallel_segmentcrop.py"+ " " + fil + " " +outfolder_cropped+"/"+newroot
#	print "crop command sent: ", cmd
	p = Popen(cmd, shell=True)

	counter=counter+1
	
	if counter == 20:
		p.wait()
	else:
		pass

# out of loop
p.wait()


############################## analize croped images #############################
 

command="find " +outfolder_cropped+"/"+ "*.jpeg > images_to_countgreen.txt"
call(command,shell=True,cwd=outfolder_cropped)

images_to_countgreen=open(outfolder_cropped+"/"+"images_to_countgreen.txt","r")
files_to_countgreen=[x.replace("\n","") for x in images_to_countgreen]
#print "counting pixels of: ", files_to_countgreen


outcount=open(outfolder+"/"+"results_pipeline_greencount.csv","w")
listoutcount=[]

for filename in files_to_countgreen:
	# filename=files_to_countgreen[0]
	# print "to segment... ", filename
	# cmd="python "+ workingfolder + "/"+ "script_segment.py " + filename
	# p = Popen(cmd, shell=True,cwd=outfolder)

	img = readgreyimage(filename)

	# maskedhsv_denoised=maskhsvdenoise(img)
	# # nameout =nameroot +"_segmented" 
	# # saveimage(nameout,maskedhsv_denoised)

	# maskedhsv_denoised_binary = cv2.medianBlur(rgb2hsv(maskedhsv_denoised)[:,:,2],5) 
	# ret,th1 = cv2.threshold(maskedhsv_denoised_binary,127,255,cv2.THRESH_BINARY) 
	# # nameout =filename[:-5] +"_segmented_binary" 
	# saveimage(nameout,th1)

	# countgreen=cv2.countNonZero(maskedhsv_denoised) 
	count=cv2.countNonZero(img) 

	
	splitfile=filename.split("/")[-1]
	splitfile=splitfile.split("_")
	filedate=splitfile[0]
	photoname=splitfile[1]
	traypos=splitfile[2].split(".")[0]

	towrite=[filedate,photoname,traypos,str(count)]
	listoutcount.append(towrite)
	
	if removeyesno=="removeyes":
		#### CAREFUL HERE, REMOVING FILES! ###
		call("rm "+filename ,shell=True,cwd=outfolder_cropped)
		######################################
	if removeyesno=="removeno":
		pass
	

# print listoutcount

for line in listoutcount:
	outcount.write(str(','.join(line)+"\n"))

outcount.close()
