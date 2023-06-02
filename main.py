from pymodbus.client import ModbusTcpClient,AsyncModbusTcpClient
import asyncio

client = AsyncModbusTcpClient("127.0.0.1",502)




async def main():
    pass




if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())