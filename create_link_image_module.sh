#!/usr/bin/env python

import sys
import os

mypythonpath=sys.path
thepath=mypythonpath[-1]
scriptsdirectory=os.getcwd()


command="ln -s " + scriptsdirectory+ os.sep +"script_image_processing.py" + " " + thepath +os.sep + "script_image_processing.py"  

print(command)