import qrcode

def generate_qr_codes():
    for x in range(1001):
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=20,
            border=1
        )
        qr.add_data(x)
        qr.make()
        img = qr.make_image(fill_color="black", back_color="white")
        type(img)
        img.save("D:\\Others\\QrCodes\\" + str(x) + ".png")

if __name__ == "__main__":
    generate_qr_codes()