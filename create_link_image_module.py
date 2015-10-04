#!/usr/bin/env python

import sys
import os
import subprocess 

# mypythonpath=sys.path
# thepath=mypythonpath[-3]
thepath="/usr/local/lib/python2.7/site-packages"
scriptsdirectory=os.getcwd()


command="ln -s " + scriptsdirectory+ os.sep +"script_image_processing.py" + " " +  "script_image_processing.py"  

print(command)
# call("hello world")
# sys.call("hello")
# subprocess.call(["echo","hello world"], shell=False)

subprocess.call([command], shell=True,cwd=thepath+os.sep)