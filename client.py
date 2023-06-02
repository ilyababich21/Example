import random

from pymodbus.client import ModbusTcpClient, ModbusSerialClient
import time
# print([17] * 10)
client = ModbusTcpClient( "127.0.0.1", port=502)

# client = ModbusSerialClient(  port="COM9", baudrate=256000)
sttit = time.time()


while True:
    for i in range(1,201):

        result = client.write_registers(0,[random.randint(0, 350) for _ in range(15)],i)
        # time.sleep(1)
    time.sleep(0.5)

# for elem in range(100):
#     sttt = time.time()
#     for elem in range(200):
#         start = time.time()
#         result = client.read_holding_registers(0,10,1)
#         # print(result.registers, "            ",time.time()-start)
#
#     print("All time: ",time.time()-sttt)

print("Alllllllllllllllll time: ",time.time()-sttit)

#
#
# result = client.read_holding_registers(0,10,1)
# print(result.registers)



# slaves = list(range(1,101))
# print(slaves)
# di={}
# for elem in slaves:
#     di[f"{elem}"]= [random.randint(0, 17000) for i in range(2)]
#
# print(di)
