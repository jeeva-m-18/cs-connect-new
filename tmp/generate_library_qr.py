import qrcode

url = "https://cs-connect.onrender.com/library"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
# Save the QR code image into the Antigravity artifacts directory
artifacts_dir = "C:\\Users\\LENOVO\\.gemini\\antigravity\\brain\\0a2b9020-1492-4a81-b401-716b1b9134cb\\artifacts"

import os
if not os.path.exists(artifacts_dir):
    os.makedirs(artifacts_dir)

img.save(os.path.join(artifacts_dir, "library_qr.png"))
print("QR Code generated successfully at:", os.path.join(artifacts_dir, "library_qr.png"))
