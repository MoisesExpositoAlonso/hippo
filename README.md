# HIPPO: python functions and wrappers for High-throughput Imaging of Plant Organs
### Moises Exposito-Alonso
### moisesexpositoalonso@gmail.com
### moisesexpositoalonso.wordpress.com

This small python module heavily depends on the Open Computer Vision (OpenCV) and the Subprocess modules of python2.7. 

It contains some functions for segmentation of green areas of plant pictures. While the functions file can be generaly used, the pipeline file is very customized for the specific task I needed for my analyses: reading thousands of image files, segment them and crop them in squares containing one plant each.

### Scheme of pipeline steps ###
#### read all images in a directory
Get the date of the file
Load the index of the trays
#### crop and save all pot images with the date, original image name and coordinates of pot
Number of images is 49trays * 40pots * 20timepictures = 39200 pictures to analyze, then better to parallelize
#### segment all images
Append in to a single file with photo number, date and location

