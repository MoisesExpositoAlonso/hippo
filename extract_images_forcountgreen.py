import sys, os, time

from subprocess import *

# 1a ## folder get 

infolder="/ebio/abt6_projects9/ath_1001G_image_pheno/data/greenhouse_drought_experiment/alljpg"

# 1b ## images list
command="find " +infolder+"/"+ "*.JPG > images_to_analyze.txt"
call(command,shell=True)
# read list
images_to_analyze=open(infolder+"/"+"images_to_analyze.txt","r")
filesimage=[x.replace("\n","") for x in images_to_analyze]



# 2 ## File info
# 3 ## generate
counterimage=1

index_images=[]
for fil in filesimage:
	(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(fil)
#print "last modified: %s" % time.ctime(mtime)
	mytime=time.ctime(mtime)
	mytime=mytime.replace("  "," ").split(" ")

	timestring="2015"+"-"+mytime[1]+"-"+mytime[2]
	
	#mytime=time.ctime(os.path.getctime(fil))
	#mytime=mytime.split(" ")
	#listposition=[1,2,4]
	#finaltime=[x[1] for x in enumerate(mytime) if x[0] in listposition]
	#timestring=finaltime[2]+"-"+finaltime[0]+"-"+finaltime[1]

	if timestring == "2015-Jul-29"  and counterimage == 32:
		counterimage=counterimage+1
		pass
	else:
		pass
 
	row=[ str(fil),str(timestring),str(counterimage)]
	index_images.append(row)
	print row

	counterimage=counterimage+1

	if counterimage == 50:
		counterimage=1
	else:
		pass

# 4 ## write output

output=open(infolder+"/"+"index_images.txt","w")
for line in index_images:
	output.write(str(','.join(line)+"\n"))

output.close()

print "csv written"

