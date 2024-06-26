from rfm69 import RFM69
from machine import SPI, Pin

CS = Pin(15, Pin.OUT, value=1)

#reset = Pin(22, Pin.OUT)
reset = None
# spi = SoftSPI(sck=Pin(10), mosi=Pin(11), miso=Pin(8), baudrate=200_000, firstbit=SoftSPI.MSB)

spi = SPI(1, baudrate=50_000,
          polarity=0,
          phase=0,
          bits=8,
          sck=Pin(10), mosi=Pin(11), miso=Pin(8))

rfm69 = RFM69(spi, CS, reset, frequency=868)

# Optionally set an encryption key (16 byte AES key). MUST match both
# on the transmitter and receiver (or be set to None to disable/the default).
rfm69.encryption_key = (
    b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
)

# Print out some chip state:
print("Temperature: {0}C".format(rfm69.temperature))
print("Frequency: {0}mhz".format(rfm69.frequency_mhz))
print("Bit rate: {0}kbit/s".format(rfm69.bitrate / 1000))
print("Frequency deviation: {0}hz".format(rfm69.frequency_deviation))
import time

try:
#    rfm69.idle()

    # Send a packet.  Note you can only send a packet up to 60 bytes in length.
    # This is a limitation of the radio packet size, so if you need to send larger
    # amounts of data you will need to break it into smaller send calls.  Each send
    # call will wait for the previous one to finish before continuing.
    print("Sending hello world message...")

    i = 0
    while i < 10:
        rfm69.send(bytes("Hello world!\r\n", "utf-8"))
        time.sleep(2)
        print("Sent hello world message!")
        i += 1

    # Wait to receive packets.  Note that this library can't receive data at a fast
    # rate, in fact it can only receive and process one 60 byte packet at a time.
    # This means you should only use this for low bandwidth scenarios, like sending
    # and receiving a single message at a time.
    print("Waiting for packets...")
    packet = rfm69.receive(timeout=1)
    # Optionally change the receive timeout from its default of 0.5 seconds:
    # packet = rfm69.receive(timeout=5.0)
    # If no packet was received during the timeout then None is returned.
    if packet is None:
        # Packet has not been received
        print("Received nothing! Listening again...")
        print("Temp", rfm69.temperature)
    else:
        # Received a packet!
        # Print out the raw bytes of the packet:
        print("Received (raw bytes): {0}".format(packet))
        # And decode to ASCII text and print it too.  Note that you always
        # receive raw bytes and need to convert to a text format like ASCII
        # if you intend to do string processing on your data.  Make sure the
        # sending side is sending ASCII data before you try to decode!
        packet_text = str(packet, "ascii")
        print("Received (ASCII): {0}".format(packet_text))
except KeyboardInterrupt:
    rfm69.sleep()
