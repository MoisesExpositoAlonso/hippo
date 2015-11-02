from script_image_processing import *
from moi import *
import sys
import os
from subprocess import *


############################## FOLDER TO WORK #############################

#outfolder="/Users/moisesexpositoalonso/image1001g/tmp"
#infolder="/Users/moisesexpositoalonso/image1001g"


#outfolder=sys.argv[1]
#infolder=sys.argv[2]


infolder='/ebio/abt6_projects9/ath_1001G_image_pheno/scripts'
outfolder='/ebio/abt6_projects9/ath_1001G_image_pheno/tmp'


print "reading from ", infolder
print "writing to ",outfolder



workingfolder=os.getcwd()

############################## PARSE JPG FILES #############################
### Find all the JPG files in a folder
command="find " +infolder+"/"+ "*.JPG >" +outfolder+"/"+"images_to_analyze.txt"
print command
call(command,shell=True)

images_to_analyze=open(outfolder+"/"+"images_to_analyze.txt","r")
filesimage=[x.replace("\n","") for x in images_to_analyze]

### Read the image and crop

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
	
	### send a job of cropping
	cmd="python script_crop_tray.py"+" "+fil + " " +outname
	# print cmd
	p = Popen(cmd, shell=True)
	p.wait()

############################## analize croped images #############################
 

command="find " +outfolder+"/"+ "*.jpeg > images_to_countgreen.txt"
call(command,shell=True,cwd=outfolder)

images_to_countgreen=open(outfolder+"/"+"images_to_countgreen.txt","r")
files_to_countgreen=[x.replace("\n","") for x in images_to_countgreen]

outcount=open(outfolder+"/"+"results_pipeline_greencount.csv","w")
listoutcount=[["date","imagename","position","greencount"]]

for filename in files_to_countgreen:
	# filename=files_to_countgreen[0]
	# cmd="python "+ workingfolder + "/"+ "script_segment.py " + filename
	# p = Popen(cmd, shell=True,cwd=outfolder) # if I make this parallel, I have to include a step to count the pixels, and that means that i need to generate the images
	
	print "to segment... ", filename


	img = readcolimage(filename)

	maskedhsvdenoised=maskhsvdenoise(img)
	# nameout =filename.split("/")[-1].split(".")[0] +"_segmentedhsv" 
	# saveimagejpeg(name=outfolder+"/"+nameout,image=maskedhsvdenoised)
	
	maskedhsvdenoisedgray=rgb2gray(maskedhsvdenoised)
	# nameout =filename.split("/")[-1].split(".")[0] +"_segmentedhsvgray" 
	# saveimagejpeg(name=outfolder+"/"+nameout,image=maskedhsvdenoisedgray)

	maskedhsv_denoised_binary = cv2.medianBlur(rgb2hsv(maskedhsvdenoised)[:,:,2],5) 
	ret,th1 = cv2.threshold(maskedhsv_denoised_binary,127,255,cv2.THRESH_BINARY) 
	# nameout =filename.split("/")[-1].split(".")[0] +"_segmented_binary" 
	# saveimagejpeg(name=outfolder+"/"+nameout,image=th1)

	countgreen=cv2.countNonZero(maskedhsvdenoisedgray ) # nothe the conversion into gray values
	countbinary=cv2.countNonZero(th1) 

	splitfile=filename.split("/")[-1]
	splitfile=splitfile.split("_")
	filedate=splitfile[0]
	photoname=splitfile[1]
	traypos=splitfile[2].split(".")[0]


	towrite=[filedate,photoname,traypos,str(countbinary),str(countgreen)]
	print towrite
	listoutcount.append(towrite)



# print listoutcount

for line in listoutcount:
	outcount.write(str(','.join(line))+"\n")

outcount.close()
