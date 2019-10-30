import pyqrcode
from pyqrcode import QRCode


def qr_code_generator(email):
    url = pyqrcode.create(email)
    url.svg("myqrcode1.svg", scale=8)