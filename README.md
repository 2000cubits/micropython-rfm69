
Work in progress
============
This libary is a work in progress with limited testing.  

Introduction
============

This is a port of the Adafruit_CircuitPython_RFM69 library of which this repo is forked from and found here:
https://github.com/adafruit/Adafruit_CircuitPython_RFM69

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

.. code-block:: python

    # Initialze RFM radio
    rfm69 = RFM69(spi, CS, RESET, RADIO_FREQ_MHZ)
