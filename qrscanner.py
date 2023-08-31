import qrcode
import image
qr = qrcode.QRCode(
    version = 15, 
    box_size = 18,
    border = 5 
)

data = "https://www.linktr.ee/codingbyumut"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fil="black",back_color = "white")
img.save("scaneqrcode.png")