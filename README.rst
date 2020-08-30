
Introduction
============

This is a port of the Adafruit_CircuitPython_RFM69 library of which this repo is forked from and found here:


MicroPython RFM69 packet radio module.  This supports basic RadioHead-compatible sending and
receiving of packets with RFM69 series radios (433/915Mhz).

.. warning:: This is NOT for LoRa radios!

.. note:: This is a 'best effort' at receiving data using pure Python code--there is not interrupt
    support so you might lose packets if they're sent too quickly for the board to process them.
    You will have the most luck using this in simple low bandwidth scenarios like sending and
    receiving a 60 byte packet at a time--don't try to receive many kilobytes of data at a time!


This has been tested on various ESP32 and ESP8266 dev boards.  For detailed information on experiments with these devices, please visit the repository below:
https://github.com/nohcpy/LoPPyIOT


Usage Example
=============
See examples/rfm69_simpletest.py for a simple demo of the usage.
Note: the default baudrate for the SPI is 5000000 (5MHz). 
The maximum setting is 10Mhz but 
transmission errors have been observed expecially when using breakout boards.
For breakout boards or other configurations where the boards are separated,
it may be necessary to reduce the baudrate for reliable data transmission.
The baud rate may be specified as an keyword parameter when initializing the board.
To set it to 1000000 use :

.. code-block:: python

    # Initialze RFM radio
    rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ,baudrate=1000000)



For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
