import qrcode

qr = qrcode.make("http://www.google.com")
qr.save("MYQR.png")
