import time
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
from pymodbus.client import ModbusTcpClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer

def jaw_open():
  print(jaw_open)
  logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 0, 0, 0]))
  time.sleep(3)
  logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))

def jaw_close():
  logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 1, 0, 0]))
  time.sleep(3)
  logger.info(jaw_1.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))

def up():
  client_2.write_register(address=1298, value=1)
  time.sleep(10)
  client_2.write_register(address=1298, value=0)

def down():
  client_2.write_register(address=1298, value=5)
  time.sleep(2)
  client_2.write_register(address=1298, value=0)

def jaw_back():
  client_1.write_register(address=1298, value=1)
  time.sleep(4)
  client_1.write_register(address=1298, value=0)

def jaw_front(time_front):
  client_1.write_register(address=1298, value=5)
  time.sleep(time_front)
  client_1.write_register(address=1298, value=0)

logger = modbus_tk.utils.create_logger("console")

client_1 = ModbusTcpClient("192.168.255.104", port=502, framer=ModbusFramer)
client_2 = ModbusTcpClient("192.168.255.105", port=502, framer=ModbusFramer)
success = client_1.connect()
success = client_2.connect()

jaw_1 = modbus_tcp.TcpMaster(host="192.168.255.5")
jaw_1.set_timeout(5.0)
logger.info("connected")

# jaw_front(3)
# up()

# client_2.write_register(address=513, value=500)
# down()

# 夾爪開
# jaw_open()

# 夾爪關
# jaw_close()

jaw_back()
