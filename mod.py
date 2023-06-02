import asyncio
import random
import time

from async_modbus import AsyncTCPClient


async def main():

    reader = await asyncio.open_connection('127.0.0.1', 500)
    client = AsyncTCPClient(reader)

    while True:


        # await asyncio.wait([read(client,i) for i in range(1,8)])

        list = await read(client)

        print(list)
        # await asyncio.sleep(1)

async def read(client):



        # reply1 = await client.read_holding_registers(slave_id=elem, starting_address=0, quantity=1)
    sttt = time.time()


    for elem in range(1,101):
        result = await client.read_holding_registers(slave_id=elem, starting_address=0, quantity=10)
        print(result)
    print("All time: ", time.time() - sttt)
    # for elem in range(1, 8):
    #     result2 = await client.read_holding_registers(slave_id=elem, starting_address=0, quantity=10)
    #     print(result2,"  salam", elem)
    # rand =  random.randint(1, 6)
    # await asyncio.sleep(rand)

        # print(elem,'   ',reply1,', ')


    # reply.append(reply1)
        # reply1 = await client.read_holding_registers(slave_id=2, starting_address=1, quantity=2)




asyncio.run(main())