import cv2

def decode_qr_link(qr_img):

    detect = cv2.QRCodeDetector()
    data_linked, points, straight_qrcode = detect.detectAndDecode(qr_img)

    return data_linked
