import Image, sys

mypicture=sys.argv[1]

im = Image.open(mypicture)

newname=mypicture[0:-3]+"png"
im.save(newname)

