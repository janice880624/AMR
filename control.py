import sys
import serial
import time
from pynput import keyboard

#add logging capability
import logging
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp

def stop():
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[0, 0, 0, 0]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))

def front(speed):
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 0, 1, 0]))

def back(speed):
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 1, 0, 1]))

def right(speed):
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 0]))

def left(speed):
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 1, 1]))

def right_all(speed):
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))

def left_all(speed):
    logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
    logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 1, 1]))

logger = modbus_tk.utils.create_logger("console")
input_speed = 2000

if __name__ == "__main__":
    try:
        #Connect to the slav
        master_1 = modbus_tcp.TcpMaster(host="192.168.255.1")
        master_2 = modbus_tcp.TcpMaster(host="192.168.255.3")
        master_1.set_timeout(5.0)
        master_2.set_timeout(5.0)
        logger.info("connected")

        # time.sleep(5)
        # front(input_speed)
        # time.sleep(5)
        # back(input_speed)
        # time.sleep(5)
        # right(input_speed)
        # time.sleep(5)
        # left(input_speed)
        # time.sleep(5)
        # stop(0)
        # left_all(input_speed)
        stop()

        
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))