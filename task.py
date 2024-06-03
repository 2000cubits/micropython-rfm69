import asyncio

from rfm69 import RFM69
from machine import SPI, Pin


class Rfm69Task:

    def __init__(self, transciever: RFM69):
        self._t = transciever
        self.coro = asyncio.create_task(self._run())

    async def _run(self):
        while True:
            await asyncio.sleep(1)


async def main():
    t = Rfm69Task(RFM69(
        spi=SPI(1, baudrate=50_000,
                polarity=0,
                phase=0,
                bits=8,
                sck=Pin(10), mosi=Pin(11), miso=Pin(8)),
        cs=Pin(15, Pin.OUT, value=1),
        reset=Pin(22, Pin.OUT),
        interrupt=Pin(14),
        frequency=868
    ))

    while True:
        await asyncio.sleep(100)


asyncio.run(main())
