#!/usr/bin/env python3

import asyncio
import logging
import os

# --------------------------------------------------------------------------- #
# import the various client implementations
# --------------------------------------------------------------------------- #
from helper import get_commandline
from pymodbus.client import (
    AsyncModbusSerialClient,
    AsyncModbusTcpClient,
    AsyncModbusTlsClient,
    AsyncModbusUdpClient,
)


_logger = logging.getLogger()


def setup_async_client(description=None, cmdline=None):
    """Run client setup."""


    client = AsyncModbusTcpClient(
        "127.0.0.1",
        port=502,  # on which port

    )



    return client


async def run_async_client(client, modbus_calls=None):
    """Run sync client."""
    _logger.info("### Client starting")
    await client.connect()
    assert client.connected
    if modbus_calls:
        await modbus_calls(client)
    await client.close()
    _logger.info("### End of Program")


