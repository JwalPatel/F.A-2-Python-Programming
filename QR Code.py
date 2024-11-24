import pyqrcode

name = "This QR code was created by Jwal Patel"
k = pyqrcode.create(name)
k.png('QR code.png', scale = 10)

import os
os.system('test.png')
