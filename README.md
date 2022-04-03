# Python_BT_central_big_data

Bluetooth peripheral (server side) - Python version

This program can receive a high volume of data via bluetooth BLE. The data is sent by the accompanion program "
received is splitted into chunks. These chunks are reassembled by this Python program all. Further the extra protocol elements used to be able to reassemble the chunks are removed. 

This application can be used together with

    Zephyr_BT_periph_big_data
    
## Requirements
bleak installed
source: https://github.com/hbldh/bleak

`pip install bleak`


