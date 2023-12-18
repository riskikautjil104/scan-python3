import pyqrcode
from pyqrcode import QRCode
from PIL import Image

# Membuat QR Code
s = "https://bit.ly/DiesNatalisHMTI"
qr = pyqrcode.create(s)

# Menyimpan QR Code sebagai gambar
qr.png('qr_code.png', scale=6)

# Membuka gambar QR Code dan logo
qr_image = Image.open('qr_code.png')
logo_image = Image.open('logo.jpg')

# Mengubah ukuran logo sesuai kebutuhan
logo_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)
logo_image = logo_image.resize(logo_size)

# Mengonversi gambar QR Code ke mode RGB
qr_image = qr_image.convert("RGB")

# Menggabungkan logo ke dalam gambar QR Code
qr_image.paste(logo_image, (qr_image.size[0] // 2 - logo_image.size[0] // 2, qr_image.size[1] // 2 - logo_image.size[1] // 2), logo_image)

# Menyimpan gambar QR Code dengan logo
qr_image.save('HMTIDIES9.png')
