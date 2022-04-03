# Python_BLE_central_big_data

Bluetooth peripheral (server side) - Python version

This program is the counterpart of the accompanion program ```Zephyr_BT_periph_big_data```. The latter can send high volume data via Bluetooth BLE, by splitting the data into small chunks and inserting extra information so that the receiving side (the central program) is able to reassemble the received data chunks, into the high volume data as sent by the peripheral program. This central program does this reassembling of received data.

The central part is both available as a Python script (this repo) as as a C program.

This application can be used together with

    Zephyr_BLE_periph_big_data
    
## Requirements
This script uses ```bleak``` a GATT client software, capable of connecting to BLE devices acting as GATT servers

source: https://github.com/hbldh/bleak

`pip install bleak`


