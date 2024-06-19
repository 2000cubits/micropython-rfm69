import asyncio
from rfm69 import RFM69, OutgoingPacket
from machine import SPI, Pin


cs = Pin(15, Pin.OUT, value=1)
reset = Pin(22, Pin.OUT)
spi = SPI(1, baudrate=50_000, polarity=0, phase=0, bits=8, sck=Pin(10), mosi=Pin(11), miso=Pin(8))
interrupt = Pin(14)

enc = b"mysecretpassword"
print("Using encryption:", enc.decode("UTF-8"))

rfm69 = RFM69(spi, cs=cs, reset=reset, interrupt=interrupt, frequency=868)
# Optionally set an encryption key (16 byte AES key). MUST match both
# on the transmitter and receiver (or be set to None to disable/the default).
rfm69.tx_power = enc


async def send_packets():
    while True:
        print("Sending test message to node 1")
        r = await rfm69.send(OutgoingPacket(bytes("Hello world!\r\n", "utf-8"), 1))
        print("Sent hello world message!", r)
        await asyncio.sleep(5)


async def receive_packets():
    while True:
        # Wait to receive packets.  Note that this library can't receive data at a fast
        # rate, in fact it can only receive and process one 60 byte packet at a time.
        # This means you should only use this for low bandwidth scenarios, like sending
        # and receiving a single message at a time.
        print("Waiting for packets...")
        packet = await rfm69.receive(timeout=1)
        # Optionally change the reception timeout from its default of 0.5 seconds:
        # packet = rfm69.receive(timeout=5.0)
        # If no packet was received during the timeout then None is returned.
        if packet is None:
            # Packet has not been received
            print("Received nothing! Listening again...")
        else:
            # Received a packet!
            # Print out the raw bytes of the packet:
            print("Received (raw bytes): {0}".format(packet))
            # And decode to ASCII text and print it too.  Note that you always
            # receive raw bytes and need to convert to a text format like ASCII
            # if you intend to do string processing on your data.  Make sure the
            # sending side is sending ASCII data before you try to decode!
            packet_text = str(packet.data, "ascii")
            print("Received (ASCII): {0}".format(packet_text))


async def main():
    # Print out some chip state:
    print("Temperature: {0}C".format(rfm69.temperature))
    print("Frequency: {0}mhz".format(rfm69.frequency_mhz))
    print("Bit rate: {0}kbit/s".format(rfm69.bitrate / 1000))
    print("Frequency deviation: {0}hz".format(rfm69.frequency_deviation))

    asyncio.create_task(receive_packets())
    asyncio.create_task(send_packets())

    while True:
        await asyncio.sleep(100)

loop = asyncio.get_event_loop()

try:
    print("RUNNNING MAIN")
    asyncio.run(main())
except KeyboardInterrupt:
    print("Interrupted by CTRL+C")
finally:
    asyncio.new_event_loop()
