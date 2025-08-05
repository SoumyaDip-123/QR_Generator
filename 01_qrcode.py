import qrcode
data = "https://github.com/SoumyaDip-123"
qr = qrcode.make(data)
qr.save("qrcode.png")
print("Qrcode Generate Successfully!")
