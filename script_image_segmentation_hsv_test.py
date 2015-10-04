#### PIPELINE FOR IMAGE ANALYSIS OF ARABIDOPSIS ROSETES  ####
#@#
# these need to be installed ... in mac easy with brew ... or pip ....

from script_image_processing import *
from moi import *

filename='ara.jpg'
filename='araqr.jpg'
filename='P1000363.JPG'
# filename='~/image/processing_1001/P1000363.jpeg'


image=readcolimage(filename)

separatehsv=splithsvandsave(image)
saveimage('hsvseparated_1_saturation',separatehsv[1])
saveimage('hsvseparated_2_hue',separatehsv[2])
saveimage('hsvseparated_0_value',separatehsv[0])



croped=crop(image,x1=220, x2=714, y1=573,y2=1028)
saveimage(name,croped)

