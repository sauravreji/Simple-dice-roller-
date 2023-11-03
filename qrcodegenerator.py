import qrcode


data = input("Enter what you want to convert to a qrcode: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)


qr.add_data(data)


qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")


img.save("pic.png")

print("QR code generated and saved as my_qr_code.png")