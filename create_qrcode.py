import qrcode
img = qrcode.make("https://www.linkedin.com/in/siham-tabbaa/")
img.save("qr-linkedin.png")
