# -*- coding: utf-8 -*-

import sys
import asyncio
import platform

from bleak import BleakClient


# you can change these to match your device or override them from the command line
# you can find these UUID via bleak service explorer
CHARACTERISTIC_UUID = "00002a37-0000-1000-8000-00805f9b34fb"


ADDRESS = (
# address of Arduino nano 33 ble running BLE_peripheral
    "EA:D0:C7:96:E2:17"
    if platform.system() != "Darwin"
    else "B9EA5233-37EF-4DD6-87A8-2A875E821C46"
)


def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    global ReceivedPayload
    ChunkNbr = data[0]
    MoreDataFollows = data[1]

    if (ChunkNbr == 0):
        print("ChunkNbr= {0}".format(ChunkNbr))
        #first chunk
        ReceivedPayload = []

    #print("Append data to receivedPayload")
    ReceivedPayload.extend(data[2:])
    
    if (MoreDataFollows == 0):
        # no more chunks follow
        # print whole received payload
        print("{0}".format(ReceivedPayload))

async def main(address, char_uuid):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")

        await client.start_notify(char_uuid, notification_handler)
        await asyncio.sleep(5.0)
        await client.stop_notify(char_uuid)


if __name__ == "__main__":
    asyncio.run(
        main(
            sys.argv[1] if len(sys.argv) > 1 else ADDRESS,
            sys.argv[2] if len(sys.argv) > 2 else CHARACTERISTIC_UUID,
        )
    )
