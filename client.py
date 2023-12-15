import random

from pymodbus.client import ModbusTcpClient, ModbusSerialClient
import time
# print([17] * 10)
client = ModbusTcpClient( "127.0.0.1", port=502)

# client = ModbusSerialClient(  port="COM9", baudrate=256000)
sttit = time.time()

print(8//8)
while True:
    # for i in range(1,50):
    #
    #     result = client.write_registers(0,[random.randint(250, 450) for _ in range(15)],i)

    result = client.write_registers(0, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(120, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(240, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(360, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(480, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(600, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(720, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(840, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(960, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(1080, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(1200, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(1320, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(1440, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(1560, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(1680, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(1800, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(1920, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(2040, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(2160, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(2280, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(2400, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(2520, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(2640, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(2760, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(2880, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(3000, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(3120, [random.randint(250, 450) for _ in range(120)], 1)
    result = client.write_registers(3240, [random.randint(250, 450) for _ in range(120)], 1)
    # time.sleep(1)
    # time.sleep(0.1)

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
