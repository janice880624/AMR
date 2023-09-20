# -*- coding: utf-8 -*-
import cv2
import numpy as np



check=[0,0,0]
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("无法打开摄像头")
    exit()


def calculate_center_point(points):

    center_x = sum(point[0] for point in points) / 4
    center_y = sum(point[1] for point in points) / 4
    
    return center_x, center_y

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(1080,960))
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    try:
       
        if ret and check!=[1,1,1]:
            qrcode = cv2.QRCodeDetector()# 建立 QRCode 偵測器
            retval, decoded_info, points, straight_qrcode = qrcode.detectAndDecodeMulti(frame)
            if points is not None:
                
                points1 = np.round(points[0][0])#左上
                points2 = np.round(points[0][1])#右上
                points3 = np.round(points[0][2])#右下
                points4 = np.round(points[0][3])#左下
                print(points1,points2,points3,points4)
                coordinate=[(int(points1[0]), int(points1[1])),(int(points2[0]), int(points2[1])),(int(points3[0]), int(points3[1])),(int(points4[0]), int(points4[1]))]
                centerx,centery=calculate_center_point(coordinate)#正方形中心
                print(centerx,centery)

                x_length=int(points2[0]-points1[0])
                print(x_length)
                y_length=int(points4[1]-points1[1])
                print(y_length)

                print("面積" ,(x_length*y_length))
                print("-----------------")
                    
                  
                #%%檢查傾斜
                print(int(points3[1]-points2[1]))

                cv2.circle(frame,(int(centerx),int(centery)), 8, (0, 255, 255), -1)#印出中心點
                # cv2.circle(frame,(int(centerx),int(centery)), 5, (255, 255, 0), -1)#印出正方形中心
                cv2.circle(frame,(int(points1[0]), int(points1[1])), 5, (255, 0, 0), -1)#印出右下

            cv2.imshow("Processed Video", frame)
        

            
            
            
        
        
    except AttributeError as e:
        print("发生了一个异常:", e)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
