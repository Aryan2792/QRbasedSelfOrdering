import qrcode

img = qrcode.make(data='127.0.0.1:8000')
img.save('code.png')