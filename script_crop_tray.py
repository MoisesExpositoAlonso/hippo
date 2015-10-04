#### PIPELINE FOR IMAGE ANALYSIS OF ARABIDOPSIS ROSETES  ####

# these need to be installed ... in mac easy with brew ... or pip ....

# import script_image_processing
# import moi

from script_image_processing import *
from moi import *


### Read image

# filename='ara.jpg'
# filename='araqr.jpg'
filename='P1000363.JPG'
im=readcolimage(filename)
type(im)
height, width, channels = im.shape
print height, width, channels


## get the index of pot positions

fileindex="index_pots_pertray.tsv"
# print fileindex
# indexpots=open(fileindex,"r")
# indexpots=[x.replace("\n","").split("\t") for x in indexpots]
# print indexpots

table=readtabtable(filename=fileindex)
print table


rows= ["A", "B",  "C",  "D", "E"] 
columns=[1,2,3,4,5,6,7,8]


for r in rows:
 for c in columns:
  # if str(r)+str(c) any 
  print str(r)+str(c)
  nameout =filename[:-4] +"_" +str(r)+str(c)
  for t in table:
   if "row" in t:
    continue
   if str(t[0]) == r and float (t[1]) ==float(c):
    # print t[2:6]
    x1= int(t[2]) -20
    x2= int(t[3]) +20
    y1= int(t[4]) -20
    y2= int(t[5]) +20
    print [x1,x2,y1,y2]
    cropim=crop(im,x1=x1,x2=x2,y1=y1,y2=y2)
    saveimage(name=nameout,image=cropim) 
