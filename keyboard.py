import sys
import time
import tty, termios
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp

def stop():
  logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[0, 0, 0, 0]))
  logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))

def front(speed):
  logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
  logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 0, 1, 0]))
  time.sleep(0.5)
  stop()

def back(speed):
  logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
  logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 1, 0, 1]))
  time.sleep(0.2)
  stop()

def right(speed):
  logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
  logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 0]))
  time.sleep(1)
  stop()

def left(speed):
  logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
  logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 1, 1]))
  time.sleep(1)
  stop()

def aa(speed):
  logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
  logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))
  time.sleep(0.5)
  stop()

def bb(speed):
  logger.info(master_2.execute(3, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[speed, speed, speed, speed]))
  logger.info(master_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 1, 1, 0, 0]))
  time.sleep(0.5)
  stop()

logger = modbus_tk.utils.create_logger("console")
input_speed = 1000

if __name__ == "__main__":
  try:
    master_1 = modbus_tcp.TcpMaster(host="192.168.255.4")
    master_2 = modbus_tcp.TcpMaster(host="192.168.255.3")
    master_1.set_timeout(5.0)
    master_2.set_timeout(5.0)
    logger.info("connected")

    while True:

      fd = sys.stdin.fileno()
      old_settings = termios.tcgetattr(fd)

      try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)

      finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        if ch == 'w':
          print("f")
          front(input_speed)

        elif ch == 'a':
          print("b")
          left(input_speed)

        elif ch == 's':
          print("l")
          back(input_speed)

        elif ch == 'd':
          print("r")
          right(input_speed)

        elif ch == 'e':
          print("ll")
          aa(input_speed)

        elif ch == 'q':
          print("rr")
          bb(input_speed)

        elif ch == "f":
          print("s")
          stop()

        elif ch == 'z':
          print("shutdown")
          break

        else:
          stop()

  except modbus_tk.modbus.ModbusError as e:
      logger.error("%s- Code=%d" % (e, e.get_exception_code()))