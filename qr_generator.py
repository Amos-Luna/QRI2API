import qrcode

link_example = "https://github.com/Amos-Luna/QRI2API"
qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=5)

qr.add_data(link_example)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')

#upload this image to uvicorn server as example to try out API functionality
img.save('qr_img_example.png')