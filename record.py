import time
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
from pymodbus.client import ModbusTcpClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer

client_1 = ModbusTcpClient("192.168.255.104", port=502, framer=ModbusFramer)
client_2 = ModbusTcpClient("192.168.255.105", port=502, framer=ModbusFramer)
success = client_1.connect()

# 夾爪
# 往前
# print('夾爪往前')
# client_1.write_register(address=1298, value=5)
# time.sleep(8)
# client_1.write_register(address=1298, value=0)

# time.sleep(0.5)
# 往後
print('夾爪往後')
client_1.write_register(address=1298, value=1)
time.sleep(8)
client_1.write_register(address=1298, value=0)


# 上下平台
# client_2.write_register(address=513, value=200)
# client_2.write_register(address=1298, value=1)
# time.sleep(1)
# client_2.write_register(address=1298, value=0)
