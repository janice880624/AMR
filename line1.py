from pymodbus.client import ModbusTcpClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer
import time

client = ModbusTcpClient("192.168.255.5", port=502, framer=ModbusFramer)
success = client.connect()

print('start')
print('motor go ahead')
time.sleep(2)
client.write_register(address=513, value=100)

client.write_register(address=1298, value=1)
time.sleep(1)
client.write_register(address=1298, value=0)


time.sleep(0.5)
print('motor step back')

client.write_register(address=1298, value=5)
time.sleep(1)
client.write_register(address=1298, value=0)
\
print('stop')