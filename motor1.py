# this motor is control the motor 1

import time
import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

master = modbus_rtu.RtuMaster(serial.Serial(port="COM4",baudrate=9600, bytesize=8, parity='N', stopbits=1))  
master.set_timeout(5.0)

# ------------------------------ #
# define speed  Sn201(0201H) => 513
# ------------------------------ #
print('motor go ahead')
master.execute(1, cst.WRITE_SINGLE_REGISTER, 513, output_value=-100)

# ------------------------------ #
# turn on/off  Hn617(0511H) => 1298
# ------------------------------ #
master.execute(1, cst.WRITE_SINGLE_REGISTER, 1298, output_value=1)
time.sleep(2)
master.execute(1, cst.WRITE_SINGLE_REGISTER, 1298, output_value=0)

print('motor step back')
master.execute(1, cst.WRITE_SINGLE_REGISTER, 513, output_value=100)

master.execute(1, cst.WRITE_SINGLE_REGISTER, 1298, output_value=1)
time.sleep(1)
master.execute(1, cst.WRITE_SINGLE_REGISTER, 1298, output_value=0)