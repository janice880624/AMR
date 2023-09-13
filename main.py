import cv2
import time
import numpy as np
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
from pymodbus.client import ModbusTcpClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer

def jaw_open():
    logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 0, 0, 0]))
    time.sleep(1)
    logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))
    print("jaw_open finished")

def jaw_close():
    logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 1, 0, 0]))
    time.sleep(2)
    logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))
    print("jaw_close finished")

def jaw_up(t):
    logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 1]))
    client_2.write_register(address=1298, value=1)
    time.sleep(t)
    client_2.write_register(address=1298, value=0)
    logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))
    print("jaw_up finished")
    jaw_stop()

def jaw_down(t):
    logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 1]))
    client_2.write_register(address=1298, value=5)
    time.sleep(t)
    client_2.write_register(address=1298, value=0)
    logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))
    print("jaw_down finished")
    jaw_stop()

def jaw_back(t):
    logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 1, 0]))
    client_1.write_register(address=1298, value=1)
    time.sleep(t)
    client_1.write_register(address=1298, value=0)
    logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))
    print("jaw_back finished")
    jaw_stop()

def jaw_front(t):
    logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 1, 0]))
    client_1.write_register(address=1298, value=5)
    time.sleep(t)
    client_1.write_register(address=1298, value=0)
    logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))
    print("jaw_front finished")
    jaw_stop()

def jaw_1low():
    client_1.write_register(address=513, value=100)
    jaw_stop()

def jaw_stop():
    client_1.write_register(address=1298, value=0)
    client_2.write_register(address=1298, value=0)

def client1_speed(s):
    client_1.write_register(address=513, value=s)

def client2_speed(s):
    client_2.write_register(address=513, value=s)

def stop():
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[0, 0, 0, 0]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))

def front(speed, s):
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 0, 1, 0]))
    time.sleep(s)
    stop()

def back(speed, s):
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 1, 0, 1]))
    time.sleep(s)
    stop()

def right(speed, s):
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 0]))
    time.sleep(s)
    stop()

def left(speed, s):
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 1, 1]))
    time.sleep(s)
    stop()

def aa(speed, s):
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))
    time.sleep(s)
    stop()

def bb(speed, s):
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 1, 1, 0, 0]))
    time.sleep(s)
    stop()

def calculate_center_point(points):
    center_x = sum(point[0] for point in points) / 4
    center_y = sum(point[1] for point in points) / 4
    return center_x, center_y

def get_centerx_centery(frame, qrcode):
    retval, decoded_info, points, straight_qrcode = qrcode.detectAndDecodeMulti(frame)
    if points is not None:
        points1 = np.round(points[0][0]) # 左上
        points2 = np.round(points[0][1]) # 右上
        points3 = np.round(points[0][2]) # 右下
        points4 = np.round(points[0][3]) # 左下
        coordinate = [(int(points1[0]), int(points1[1])), (int(points2[0]), int(points2[1])),(int(points3[0]), int(points3[1])), (int(points4[0]), int(points4[1]))]
        centerx, centery = calculate_center_point(coordinate)
        return centerx, centery, points1, points2, points3, points4
    else:
        print("No QRCode points found")
        return None

def draw_circles_on_frame(frame, centerx, centery, points1, points2, points3, points4):
    cv2.circle(frame, (int(centerx),int(centery)), 8, (0, 255, 255), -1)  # 印出中心點
    cv2.circle(frame, (int(centerx), int(centery)),5, (255, 255, 0), -1)  # 印出正方形中心
    cv2.circle(frame, (int(points1[0]), int(points1[1])), 5, (255, 0, 0), -1)  # 印出左上
    cv2.circle(frame, (int(points2[0]), int(points2[1])), 5, (0, 255, 0), -1)  # 印出右上
    # cv2.circle(frame, (int(points3[0]), int(points3[1])), 5, (0, 0, 255), -1)  # 印出右下
    # cv2.circle(frame, (int(points4[0]), int(points4[1])), 5, (0, 0, 0), -1)  # 印出左下

if __name__ == "__main__":
    try:
        check = [0, 0, 0]
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        qrcode = cv2.QRCodeDetector()

        if not cap.isOpened():
            print("can't open camera")
            exit()

        while True:
            ret, frame = cap.read()
            frame = cv2.resize(frame,(1080,960))
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            try:
                logger = modbus_tk.utils.create_logger("console")
                input_speed = 1000

                master_1 = modbus_tcp.TcpMaster(host="192.168.255.4") # master_1 => relay
                master_2 = modbus_tcp.TcpMaster(host="192.168.255.3") # master_2 => I/O
                jaw_1 = modbus_tcp.TcpMaster(host="192.168.255.5") # jaw_1 => jaw
                master_1.set_timeout(5.0)
                master_2.set_timeout(5.0)
                jaw_1.set_timeout(5.0)

                client_1 = ModbusTcpClient("192.168.255.105", port=502, framer=ModbusFramer) # client_1 => front/back
                client_2 = ModbusTcpClient("192.168.255.104", port=502, framer=ModbusFramer) # client_2 => up/down
                success = client_1.connect()
                success = client_2.connect()

                logger.info("connected")

                x_value = 601 #左右標準答案
                y_value = 520 #前後標準答案
                check_area = 14606 #面積標準答案

                if ret and check != [1, 1, 1]:

                    # %% Check right/left
                    while check[0] == 0:
                        
                        ret, frame = cap.read()
                        frame = cv2.resize(frame,(1080,960))
                        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                        
                        if not ret:
                            print("Failed to grab frame")
                            break
                        
                        result1 = get_centerx_centery(frame, qrcode)
                        
                        if result1 is not None:
                            centerx1, centery1, points11, points12, points13, points14 = result1
                            draw_circles_on_frame(frame, centerx1, centery1, points11, points12, points13, points14)

                            print("centerx1 => ", points12[0])

                            need_x = int(points12[0] - x_value)
                            
                            print("x need => ", need_x)
                            print("-----------------")

                            if -5 < need_x < 5:
                                check[0] = 1
                                break
                            else:
                                check[0] = 0
                                
                                if need_x > -5:
                                    back(input_speed, 0.5)
                                    print("move right")
                                if  need_x < 5:
                                    front(input_speed, 0.5)
                                    print("move left")
                        else:
                            continue

                        cv2.imshow("Processed Video", frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break

                        print("=============")
                        time.sleep(3)  # or any other appropriate delay

                        print("front/back finished")

                    # %% Check tilt
                    while check[1] == 0:
                        ret, frame = cap.read()
                        frame = cv2.resize(frame,(1080,960))
                        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                        
                        if not ret:
                            print("Failed to grab frame")
                            break
                        
                        result2 = get_centerx_centery(frame, qrcode)
                        if result2 is not None:
                            centerx2, centery2, points21, points22, points23, points24 = result2
                            draw_circles_on_frame(frame, centerx2, centery2, points21, points22, points23, points24)

                            need_z = int(points23[1]-points22[1])
                            print("y need => ", need_z)
                            print("-----------------")
    
                            if -5 < int(points23[1]-points22[1]) < 5:
                                print(points23[1])
                                print(points22[1])
                                check[1] = 1
                            else:
                                check[1] = 0


                                if int(points23[1]-points22[1]) > 5:
                                    bb(input_speed, 0.5)
                                    print("turn left")
    
                                if int(points23[1]-points22[1]) < -5:
                                    aa(input_speed, 0.5)
                                    print("turn right")

                        else:
                            continue

                        cv2.imshow("Processed Video", frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break

                        print("=============")
                        time.sleep(3)  # or any other appropriate delay

                        print("tilt finished")

                   
                    # %% Check up/down
                    while check[2] == 0:

                        ret, frame = cap.read()
                        frame = cv2.resize(frame,(1080,960))
                        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                        
                        if not ret:
                            print("Failed to grab frame")
                            break
                        result3 = get_centerx_centery(frame, qrcode)
                        
                        if result3 is not None:
                            centerx3, centery3, points31, points32, points33, points34 = result3
                            draw_circles_on_frame(
                                frame, centerx3, centery3, points31, points32, points33, points34)

                            need_z = int(points12[1] - y_value)
                            print("y need => ", need_z)
                            print("-----------------")

                            if -5 < need_z < 5:
                                check[2] = 1
                            else:
                                check[2] = 0
                                
                                if need_z > -5:
                                    jaw_down(0.4)
                                    print("move down")
                                if need_z <  5:
                                    jaw_up(0.4)
                                    print("move up")
                        else:
                            continue

                        cv2.imshow("Processed Video", frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break

                        print("=============")
                        time.sleep(3)  # or any other appropriate delay

                        print("up/down finished")

                    # %% All done

            except AttributeError as e:
                print("error:", e)

            time.sleep(1)

            cap.release()

            cv2.destroyAllWindows()
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
