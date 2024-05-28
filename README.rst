Introduction
------------

MicroPython RFM69 packet radio module. This supports basic RadioHead-compatible sending and
receiving of packets with RFM69 series radios (433/915Mhz).

.. warning:: This is NOT for LoRa radios!

.. note:: This is a 'best effort' at receiving data using pure Python code--there is not interrupt
    support so you might lose packets if they're sent too quickly for the board to process them.
    You will have the most luck using this in simple low bandwidth scenarios like sending and
    receiving a 60 byte packet at a time--don't try to receive many kilobytes of data at a time!

Usage Example
=============

See tests/test_rfm69.py for a simple demo of the usage.

History
=======

Forked from https://github.com/nohcpy/MicroPython_RFM69 which is a micropython version of
original library of Adafruit https://github.com/adafruit/Adafruit_CircuitPython_RFM69.
