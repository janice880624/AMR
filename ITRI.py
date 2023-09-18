import time
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

def jaw_clow():
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


if __name__ == "__main__":
  try:
    logger = modbus_tk.utils.create_logger("console")
    input_speed = 1000

    # car motor
    master_1 = modbus_tcp.TcpMaster(host="192.168.255.4")
    master_2 = modbus_tcp.TcpMaster(host="192.168.255.3")
    master_1.set_timeout(5.0)
    master_2.set_timeout(5.0)

    client_1 = ModbusTcpClient("192.168.255.105", port=502, framer=ModbusFramer)
    client_2 = ModbusTcpClient("192.168.255.104", port=502, framer=ModbusFramer)
    success = client_1.connect()
    success = client_2.connect()

    jaw_1 = modbus_tcp.TcpMaster(host="192.168.255.5")
    jaw_1.set_timeout(5.0)
    
    logger.info("connected")

    # front(input_speed, 0.5)
    # right(input_speed, 1)

    # left(input_speed, 1)
    # back(input_speed, 17)

    # left(input_speed, 1)

    # right(input_speed, 1)
    # jaw_front(3)
    # jaw_open()
    # jaw_back(5)
    # left(input_speed, 6)
    # back(input_speed, 6)



    # jaw_back(4)
    # left(input_speed, 1)
    jaw_up(0.6)
    # back(input_speed, 6)
    # jaw_close()

    # front(input_speed, 12)
    # jaw_up(0.1)
    # right(input_speed, 1)

    # 上料
    # jaw_front(4) 
    # jaw_close()


    # 下料
    # jaw_front(4) 
    # jaw_stop()
    # jaw_open()

    # jaw_back(4)
    # jaw_stop()

    # left(input_speed, 2)
    # back(input_speed, 4)




    # front(input_speed, 1)
    # front(input_speed, 10)
    # jaw_down(0.1)

    # jaw_open()
    


    

  except modbus_tk.modbus.ModbusError as e:
      logger.error("%s- Code=%d" % (e, e.get_exception_code()))