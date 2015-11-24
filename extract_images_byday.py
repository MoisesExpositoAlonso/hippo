# Once created the index file in the infolder, Indicating the day this extracts the images and copy them in the outfolder ####
# the date format must be juch as = 2015-Jul-31

import sys
from subprocess import *

date=sys.argv[1]



infolder="/ebio/abt6_projects9/ath_1001G_image_pheno/data/greenhouse_drought_experiment/alljpg"
outfolder="/ebio/abt6_projects9/ath_1001G_image_pheno/toy_"+date+"/"
call(["mkdir",outfolder])

index=open(infolder+"/"+"index_images.txt","r")
index=[x.replace("\n","").split(",") for x in index]



for i in index:
	#print i
	if i[1]==date:
		command="cp "+i[0] + " "+outfolder
		#p=Popen(command)
		Popen(command, shell=True, stdout=PIPE,stderr=PIPE)


print "finished process ... "


