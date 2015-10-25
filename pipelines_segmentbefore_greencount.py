from script_image_processing import *
from moi import *
import sys
import os
from subprocess import *


############################## FOLDER TO WORK #############################

outfolder="/Users/moisesexpositoalonso/image1001g/tmp"
outfolder_cropped="/Users/moisesexpositoalonso/image1001g/tmp/cropped"

infolder="/Users/moisesexpositoalonso/image1001g"

# outfolder=sys.argv[1]
# outfolder_cropped=sys.argv[1]

# infolder=sys.argv[2]

# tmpfolder=outfolder+"/segmented/"
# tmpfoldercount=outfolder+"/segmented_cropped/"


workingfolder=os.getcwd()

############################## WORK WITH JPG FILES #############################
### Segment and save image and

command="find " +infolder+"/"+ "*.JPG > images_to_analyze.txt"
call(command,shell=True)

images_to_analyze=open(infolder+"/"+"images_to_analyze.txt","r")
filesimage=[x.replace("\n","") for x in images_to_analyze]


### Read the image 

import os
import time

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


### Create the new name including root of picture date of creation

	nameroot =fil.split("/")[-1].split(".")[0]
	print "this is nameroot ",nameroot
	newroot=timestring+"_"+nameroot
	outname=outfolder+"/"+newroot 
	# print newroot # example 2015_Oct_5_P1000363_A4.jpeg
	print "this is outname",outname
	
### segment before cropping
	
	img = readcolimage(fil)

	maskedhsv_denoised=maskhsvdenoise(img)
	nameout =outname +"_segmented" 
	saveimagejpeg(nameout,maskedhsv_denoised)

	# maskedhsv_denoised_binary = cv2.medianBlur(rgb2hsv(maskedhsv_denoised)[:,:,2],5) 
	# ret,th1 = cv2.threshold(maskedhsv_denoised_binary,127,255,cv2.THRESH_BINARY) ### SO FIRST THE NORMAL, THEN I CAN TRY THIS

### send a job of cropping
	cmd="python script_crop_tray.py"+" "+nameout+"jpeg" + " " +nameout
	# print cmd
	p = Popen(cmd, shell=True)
	p.wait()


############################## analize croped images #############################
 

command="find " +outfolder+"/"+ "*.jpeg > images_to_countgreen.txt"
call(command,shell=True,cwd=outfolder)

images_to_countgreen=open(outfolder+"/"+"images_to_countgreen.txt","r")
files_to_countgreen=[x.replace("\n","") for x in images_to_countgreen]

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


	splitfile=filename.split("_")
	filedate=splitfile[0].split("/")[-1]
	photoname=splitfile[1]
	traypos=splitfile[2].split(".")[0]

	towrite=[filedate,photoname,traypos,str(count)]
	listoutcount.append(towrite+"\n")



# print listoutcount

for line in listoutcount:
	outcount.write(str(','.join(line)))

outcount.close()
