# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:58:54 2023

@author: User
"""

import cv2
import time
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

    try:
       
        if ret and check!=[1,1,1]:
            qrcode = cv2.QRCodeDetector()# 建立 QRCode 偵測器
            retval, decoded_info, points, straight_qrcode = qrcode.detectAndDecodeMulti(frame)
            if points is not None:
                
                points1 = np.round(points[0][0])#右下
                points2 = np.round(points[0][1])#左下
                points3 = np.round(points[0][2])#左上
                points4 = np.round(points[0][3])#右上
                
                coordinate=[(int(points1[0]), int(points1[1])),(int(points2[0]), int(points2[1])),(int(points3[0]), int(points3[1])),(int(points4[0]), int(points4[1]))]
                centerx,centery=calculate_center_point(coordinate)#正方形中心

                x_length = int(points4[0] - points3[0])
                y_length = int(points1[1] - points3[1])
                print("area", (x_length * y_length))
                
                cv2.circle(frame,(int(320),int(240)), 8, (0, 255, 255), -1)#印出中心點
                

                cv2.circle(frame,(int(centerx),int(centery)), 5, (255, 255, 0), -1)#印出正方形中心

                print("center => ({},{})".format(int(centerx),int(centery)))
                cv2.circle(frame,(int(points1[0]), int(points1[1])), 5, (255, 0, 0), -1)#印出右下
                cv2.circle(frame,(int(points2[0]), int(points2[1])), 5, (0, 255, 0), -1)#印出左下
                # cv2.circle(frame,(int(points3[0]), int(points3[1])), 5, (0, 0, 255), -1)#印出右上
                # cv2.circle(frame,(int(points4[0]), int(points4[1])), 5, (0, 0, 0), -1)#印出左上

                time.sleep(1)

            cv2.imshow("Processed Video", frame)
        

            
            
            
        
        
    except AttributeError as e:
        print("发生了一个异常:", e)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
