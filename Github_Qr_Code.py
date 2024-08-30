import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=4,
)
qr.add_data('https://herbiyat.com/product/erecta-10-capsules/')
qr.make(fit=True)

# Create an image with the correct mode
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
img.save("Erecta-10_Capsules.png")
