import pyqrcode
import png
from pyqrcode import QRCode

s = "https://bit.ly/DiesNatalisHMTI"

url = pyqrcode.create(s)
url.png('HMTI-DIES-NATALIS.png', scale=6)