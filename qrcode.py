from pyzbar import pyzbar
import cv2

path = '2.JPG'
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cam_x = cap.get(cv2.CAP_PROP_FRAME_WIDTH)/2
cam_y = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/2

def main():

    while (cap.isOpened()):

        ret, frame = cap.read()

        if ret == True:

            cv2.circle(frame, (int(cam_x), int(cam_y)), 5, (255, 255, 255), -1)
        
            # cv2.imshow('frame', frame)

            barcodes = pyzbar.decode(frame)
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.circle(frame, (int(x + w/2), int(y + h/2)), 5, (0, 255, 255), -1)

                img = cv2.line(frame, (int(cam_x), int(cam_y)), (int(x + w/2), int(y + h/2)), (255, 0, 255), 3)

            cv2.imshow("Image", frame)
        

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break

        # image = cv2.imread(image_path)
        # barcodes = pyzbar.decode(image)

        # for barcode in barcodes:

        #     (x, y, w, h) = barcode.rect
        #     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #     cv2.circle(image, (int(x + w/2), int(y + h/2)), 5, (0, 255, 255), -1)

        #     barcodeData = barcode.data.decode("utf-8")
        #     barcodeType = barcode.type

        #     print("{} barcode: {}".format(barcodeType, barcodeData))

        # cv2.imshow("Image", image)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()