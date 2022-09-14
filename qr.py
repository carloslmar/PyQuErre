import qrcode
from PIL import Image


qr_big = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr_big.add_data('https://example.com')
qr_big.make()
img_qr_big = qr_big.make_image(fill_color="#000000", back_color="white").convert('RGB')


img_qr_big.save('result.png')