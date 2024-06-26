import qrcode

def generate_qr(data, filename='qr_img', size=300, fill_color='black', back_color='white'):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img = img.resize((size, size))
    img.save(f"{filename}.png")

while True:
    option = input("Do you want to generate QR Code? (Y/N): ").upper()
    if option == "Y":
        data = input("Enter your url: ")
        filename = input("Enter a filename for the QR code (default is 'qrimg.png'): ")
        if not filename:
            filename = 'qr_img'
        size = input("Enter the size of the QR code (default is 300): ")
        if not size:
            size = 300
        else:
            size = int(size)
        generate_qr(data, filename, size)
        break
    elif option == "N":
        break
    else:
        print("Invalid input, pls try again!!")
