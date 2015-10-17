from qrtools import QR

import sys

mypicture=sys.argv[1]

myCode = QR(filename=mypicture)
if myCode.decode():
  print myCode.data
  print myCode.data_type
  print myCode.data_to_string()
