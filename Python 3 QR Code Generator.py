import qrcode

qr = qrcode.make("firstName, lastName: 555-555-5555")
qr.save("MYQR.png")
