class _State:
    _reset_calls = 0


def reset():
    _State._reset_calls += 1


def unique_id():
    """
    http://docs.micropython.org/en/latest/library/machine.html#machine.unique_id
    """
    return (1, 2, 3, 4)


class WDT:
    """
    Create a WDT object and start it. The timeout must be given in milliseconds.
    Once it is running the timeout cannot be changed and the WDT cannot be stopped either.
    https://docs.micropython.org/en/latest/library/machine.WDT.html
    """

    def __init__(self, id=0, timeout=5000):
        self.id = id
        self.timeout = timeout

    def feed(self):
        """
        Feed the WDT to prevent it from resetting the system.
        The application should place this call in a sensible place ensuring
        that the WDT is only fed after verifying that everything is functioning correctly.
        """
        pass


class Pin:
    OUT = "out"
    IN = "in"
    PULL_UP = "pull_up"
    PULL_DOWN = "pull_dowm"
    IRQ_FALLING = 0
    IRQ_RISING = 1
    state = {}

    def __init__(self, no, mode=-1, pull=-1, *, value=None, drive=0, alt=-1):
        self.no = no
        self.in_out = mode
        self.pull = pull
        self.state[no] = 0 if value is None else value

    def value(self, on_off=None):
        if on_off is None:
            return self.state[self.no]
        else:
            self.state[self.no] = on_off

    def on(self):
        pass

    def off(self):
        pass

    def init(self, mode=- 1, pull=- 1, value=None, drive=0, alt=-1):
        pass

    def irq(self, handler=None, trigger=None, *, priority=1, wake=None, hard=False):
        pass

    def __call__(self, *args, **kwargs):
        return self.value()


class PWM:
    def __init__(self, pin, frequency=500, duty=0):
        self._pin = pin
        self._freq = frequency
        self._duty = duty

    def duty_u16(self, a):
        self._duty = a

    def freq(self, val=None):
        if val is None:
            return self._freq
        self._freq = val


class Timer:
    PERIODIC = 'periodic'
    ONE_SHOT = 'one shot'

    def __init__(self, id):
        self.id = id

    def init(self, period, mode, callback):
        self.period = period
        self.mode = mode
        self.callback = callback

    def deinit(self):
        pass


class I2C:
    """
    Construct and return a new I2C object using the following parameters:

       - *id* identifies a particular I2C peripheral.  Allowed values for
         depend on the particular port/board
       - *scl* should be a pin object specifying the pin to use for SCL.
       - *sda* should be a pin object specifying the pin to use for SDA.
       - *freq* should be an integer which sets the maximum frequency
         for SCL.

    Note that some ports/boards will have default values of *scl* and *sda*
    that can be changed in this constructor.  Others will have fixed values
    of *scl* and *sda* that cannot be changed.
    """

    def readfrom_mem_into(self, addr, memaddr, buf, addrsize=8):
        """
        Read into *buf* from the peripheral specified by *addr* starting from the
        memory address specified by *memaddr*.  The number of bytes read is the
        length of *buf*.
        The argument *addrsize* specifies the address size in bits (on ESP8266
        this argument is not recognised and the address size is always 8 bits).

        The method returns ``None``.
        """
        pass

    def readfrom_into(self, addr, buf, stop=True):
        """
        Read into *buf* from the peripheral specified by *addr*.
        The number of bytes read will be the length of *buf*.
        If *stop* is true then a STOP condition is generated at the end of the transfer.

        The method returns ``None``.
        """
        pass

    def readfrom_mem(self, addr, memaddr, nbytes, addrsize=8):
        """
        Read *nbytes* from the peripheral specified by *addr* starting from the memory
        address specified by *memaddr*.
        The argument *addrsize* specifies the address size in bits.
        Returns a `bytes` object with the data read.
        """
        pass

    def writeto_mem(self, addr, memaddr, buf, addrsize=8):
        """
        Write *buf* to the peripheral specified by *addr* starting from the
        memory address specified by *memaddr*.
        The argument *addrsize* specifies the address size in bits (on ESP8266
        this argument is not recognised and the address size is always 8 bits).

        The method returns ``None``.
        """
        pass

    def scan(self):
        """
        Scan all I2C addresses between 0x08 and 0x77 inclusive and return a list of
        those that respond.  A device responds if it pulls the SDA line low after
        its address (including a write bit) is sent on the bus.
        """
        return [0x50, ]

    def writeto(self, addr, buf, stop=True):
        """
        Write the bytes from *buf* to the peripheral specified by *addr*.  If a
        NACK is received following the write of a byte from *buf* then the
        remaining bytes are not sent.  If *stop* is true then a STOP condition is
        generated at the end of the transfer, even if a NACK is received.
        The function returns the number of ACKs that were received.
        """
        return 1

    def writevto(self, addr, vector, stop=True):
        """
        Write the bytes contained in *vector* to the peripheral specified by *addr*.
        *vector* should be a tuple or list of objects with the buffer protocol.
        The *addr* is sent once and then the bytes from each object in *vector*
        are written out sequentially.  The objects in *vector* may be zero bytes
        in length in which case they don't contribute to the output.

        If a NACK is received following the write of a byte from one of the
        objects in *vector* then the remaining bytes, and any remaining objects,
        are not sent.  If *stop* is true then a STOP condition is generated at
        the end of the transfer, even if a NACK is received.  The function
        returns the number of ACKs that were received.
        """
        pass

    def start(self):
        """
        Generate a START condition on the bus (SDA transitions to low while SCL is high).
        """
        pass

    def readfrom(self, addr, nbytes, stop=True):
        """
        Read *nbytes* from the peripheral specified by *addr*.
        If *stop* is true then a STOP condition is generated at the end of the transfer.
        Returns a `bytes` object with the data read.
        """
        pass

    def readinto(self, buf, nack=True):
        """
        Reads bytes from the bus and stores them into *buf*.  The number of bytes
        read is the length of *buf*.  An ACK will be sent on the bus after
        receiving all but the last byte.  After the last byte is received, if *nack*
        is true then a NACK will be sent, otherwise an ACK will be sent (and in this
        case the peripheral assumes more bytes are going to be read in a later call).
        """
        pass

    def init(self, scl, sda, freq=400000):
        """
        Initialise the I2C bus with the given arguments:

           - *scl* is a pin object for the SCL line
           - *sda* is a pin object for the SDA line
           - *freq* is the SCL clock rate
        """
        pass

    def stop(self):
        """
        Generate a STOP condition on the bus (SDA transitions to high while SCL is high).
        """
        pass

    def write(self, buf):
        """
        Write the bytes from *buf* to the bus.  Checks that an ACK is received
        after each byte and stops transmitting the remaining bytes if a NACK is
        received.  The function returns the number of ACKs that were received.
        """
        pass

    def __init__(self, id, scl=None, sda=None, freq=400000):
        pass


class SPI:
    """
    Construct an SPI object on the given bus, *id*. Values of *id* depend
    on a particular port and its hardware. Values 0, 1, etc. are commonly used
    to select hardware SPI block #0, #1, etc.

    With no additional parameters, the SPI object is created but not
    initialised (it has the settings from the last initialisation of
    the bus, if any).  If extra arguments are given, the bus is initialised.
    See ``init`` for parameters of initialisation.
    """

    LSB = 1
    MSB = 1

    def deinit(self):
        """
        Turn off the SPI bus.
        """
        pass

    def init(
            self, baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None,
            pins=None
    ):
        """
        Initialise the SPI bus with the given parameters:

          - ``baudrate`` is the SCK clock rate.
          - ``polarity`` can be 0 or 1, and is the level the idle clock line sits at.
          - ``phase`` can be 0 or 1 to sample data on the first or second clock edge
            respectively.
          - ``bits`` is the width in bits of each transfer. Only 8 is guaranteed to be supported by all hardware.
          - ``firstbit`` can be ``SPI.MSB`` or ``SPI.LSB``.
          - ``sck``, ``mosi``, ``miso`` are pins (machine.Pin) objects to use for bus signals. For most
            hardware SPI blocks (as selected by ``id`` parameter to the constructor), pins are fixed
            and cannot be changed. In some cases, hardware blocks allow 2-3 alternative pin sets for
            a hardware SPI block. Arbitrary pin assignments are possible only for a bitbanging SPI driver
            (``id`` = -1).
          - ``pins`` - WiPy port doesn't ``sck``, ``mosi``, ``miso`` arguments, and instead allows to
            specify them as a tuple of ``pins`` parameter.

        In the case of hardware SPI the actual clock frequency may be lower than the
        requested baudrate. This is dependant on the platform hardware. The actual
        rate may be determined by printing the SPI object.
        """
        pass

    def write_readinto(self, write_buf, read_buf):
        """
        Write the bytes from ``write_buf`` while reading into ``read_buf``.  The
        buffers can be the same or different, but both buffers must have the
        same length.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes written.
        """
        pass

    def read(self, nbytes, write=0x00):
        """
        Read a number of bytes specified by ``nbytes`` while continuously writing
        the single byte given by ``write``.
        Returns a ``bytes`` object with the data that was read.
        """
        return bytes([0x0 * nbytes])

    def write(self, buf):
        """
        Write the bytes contained in ``buf``.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes written.
        """
        pass

    def readinto(self, buf, write=0x00):
        """
        Read into the buffer specified by ``buf`` while continuously writing the
        single byte given by ``write``.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes read.
        """
        pass

    def __init__(self, id, *args, **kwargs):
        pass


class RTC:
    """
    http://docs.micropython.org/en/latest/esp8266/quickref.html#real-time-clock-rtc
    https://github.com/micropython/micropython/blob/master/lib/timeutils/timeutils.c
    https://github.com/micropython/micropython/blob/master/ports/esp8266/machine_rtc.c

    year, month, day, weekday, hour, minute, second, msecs
    """

    __shared_state = {
        'rtc_memory': '',
        'time_tuple': (2000, 1, 1, 5, 0, 0, 0, 0)
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def memory(self, data=None):
        if data is not None:
            self.__shared_state['rtc_memory'] = data

        return self.__shared_state['rtc_memory']

    def datetime(self, time_tuple=None):
        if time_tuple is not None:
            self.__shared_state['time_tuple'] = time_tuple

        return self.__shared_state['time_tuple']

    def deinit(self):
        self.__shared_state = {
            'rtc_memory': '',
            'time_tuple': (2000, 1, 1, 5, 0, 0, 0, 0)
        }


class UART:
    """
    Construct a UART object of the given id.
    """

    INV_TX: int
    CTS: int
    INV_RX: int
    RTS: int

    def deinit(self) -> None:
        """
        Turn off the UART bus.
        """
        pass

    def init(self, baudrate=9600, bits=8, parity=None, stop=1, *args, **kwargs) -> None:
        """
        Initialise the UART bus with the given parameters:

          - *baudrate* is the clock rate.
          - *bits* is the number of bits per character, 7, 8 or 9.
          - *parity* is the parity, ``None``, 0 (even) or 1 (odd).
          - *stop* is the number of stop bits, 1 or 2.

        Additional keyword-only parameters that may be supported by a port are:

          - *tx* specifies the TX pin to use.
          - *rx* specifies the RX pin to use.
          - *rts* specifies the RTS (output) pin to use for hardware receive flow control.
          - *cts* specifies the CTS (input) pin to use for hardware transmit flow control.
          - *txbuf* specifies the length in characters of the TX buffer.
          - *rxbuf* specifies the length in characters of the RX buffer.
          - *timeout* specifies the time to wait for the first character (in ms).
          - *timeout_char* specifies the time to wait between characters (in ms).
          - *invert* specifies which lines to invert.

              - ``0`` will not invert lines (idle state of both lines is logic high).
              - ``UART.INV_TX`` will invert TX line (idle state of TX line now logic low).
              - ``UART.INV_RX`` will invert RX line (idle state of RX line now logic low).
              - ``UART.INV_TX | UART.INV_RX`` will invert both lines (idle state at logic low).

          - *flow* specifies which hardware flow control signals to use. The value
            is a bitmask.

              - ``0`` will ignore hardware flow control signals.
              - ``UART.RTS`` will enable receive flow control by using the RTS output pin to
                signal if the receive FIFO has sufficient space to accept more data.
              - ``UART.CTS`` will enable transmit flow control by pausing transmission when the
                CTS input pin signals that the receiver is running low on buffer space.
              - ``UART.RTS | UART.CTS`` will enable both, for full hardware flow control.

        On the WiPy only the following keyword-only parameter is supported:

          - *pins* is a 4 or 2 item list indicating the TX, RX, RTS and CTS pins (in that order).
            Any of the pins can be None if one wants the UART to operate with limited functionality.
            If the RTS pin is given the the RX pin must be given as well. The same applies to CTS.
            When no pins are given, then the default set of TX and RX pins is taken, and hardware
            flow control will be disabled. If *pins* is ``None``, no pin assignment will be made.
        """
        pass

    def sendbreak(self) -> None:
        """
        Send a break condition on the bus. This drives the bus low for a duration
        longer than required for a normal transmission of a character.
        """
        pass

    def read(self, nbytes: Optional[Any] = None) -> bytes:
        """
        Read characters.  If ``nbytes`` is specified then read at most that many bytes,
        otherwise read as much data as possible. It may return sooner if a timeout
        is reached. The timeout is configurable in the constructor.

        Return value: a bytes object containing the bytes read in.  Returns ``None``
        on timeout.
        """
        pass

    def any(self) -> int:
        """
        Returns an integer counting the number of characters that can be read without
        blocking.  It will return 0 if there are no characters available and a positive
        number if there are characters.  The method may return 1 even if there is more
        than one character available for reading.

        For more sophisticated querying of available characters use select.poll::

         poll = select.poll()
         poll.register(uart, select.POLLIN)
         poll.poll(timeout)
        """
        pass

    def write(self, buf) -> int:
        """
        Write the buffer of bytes to the bus.

        Return value: number of bytes written or ``None`` on timeout.
        """
        pass

    def readinto(self, buf, nbytes: Optional[Any] = None):
        """
        Read bytes into the ``buf``.  If ``nbytes`` is specified then read at most
        that many bytes.  Otherwise, read at most ``len(buf)`` bytes. It may return sooner if a timeout
        is reached. The timeout is configurable in the constructor.

        Return value: number of bytes read and stored into ``buf`` or ``None`` on
        timeout.
        """
        pass

    def readline(self) -> None:
        pass
        """
        Read a line, ending in a newline character. It may return sooner if a timeout
        is reached. The timeout is configurable in the constructor.

        Return value: the line read or ``None`` on timeout.
        """
        pass

    def __init__(self, id, *args, **kwargs) -> None:
        pass


class ADC:
    """
    The ADC class provides an interface to analog-to-digital convertors, and represents a single endpoint
    that can sample a continuous voltage and convert it to a discretised value.
    """

    def __init__(self, pin: Pin):
        self.pin = pin

    def read_u16(self):
        """
        Take an analog reading and return an integer in the range 0-65535. The return value represents the raw reading
        taken by the ADC, scaled such that the minimum value is 0 and the maximum value is 65535.
        """
        return 10000

    def read_uv(self):
        """
        Take an analog reading and return an integer value with units of microvolts. It is up to the particular
        port whether this value is calibrated, and how calibration is done.
        """
        return 1000
