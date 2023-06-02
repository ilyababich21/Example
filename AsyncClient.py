import asyncio
import random
import time

from async_modbus import AsyncTCPClient



async def main():

    reader = await asyncio.open_connection('127.0.0.1', 502)
    client = AsyncTCPClient(reader)
    sttit = time.time()

    for elem in range(100):
        await read(client)
    print("AllLLLLLLLLL time: ", time.time() - sttit)


async def read(client):

    # reply1 = await client.read_holding_registers(slave_id=elem, starting_address=0, quantity=1)
    sttt = time.time()

    for elem in range(1, 201):
        result = await client.read_holding_registers(slave_id=1, starting_address=0, quantity=10)
        print(result)
    print("All time: ", time.time() - sttt)














asyncio.run(main())