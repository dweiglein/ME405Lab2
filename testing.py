import pyb
import utime
from pyb import UART

motorTimer = pyb.Timer(3, freq=20000)
motorpin1 = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
motorpin2 = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
enablepin = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.IN, pyb.Pin.PULL_UP)
motorch1 = motorTimer.channel(1, pyb.Timer.PWM, pin=motorpin1)
motorch2 = motorTimer.channel(2, pyb.Timer.PWM, pin=motorpin2)

encoderTimer = pyb.Timer(4, prescaler=0, period=0xFFFF)
encoderpin1 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN)
encoderpin2 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN)
encoderch1 = encoderTimer.channel(1, pyb.Timer.ENC_AB, pin=encoderpin1)
encoderch2 = encoderTimer.channel(2, pyb.Timer.ENC_AB, pin=encoderpin2)


def set_duty_cycle(level):
    if level <= 0:
        level = -1 * level
        motorch1.pulse_width_percent(level)
        motorch2.pulse_width_percent(0)
    else:
        motorch1.pulse_width_percent(0)
        motorch2.pulse_width_percent(level)


def read():
    count = encoderTimer.counter()
    return count



#ser = pyb.USB_VCP()
ser = pyb.UART(2, baudrate=115200, timeout = 10)

def main():
    ser = pyb.UART(2, baudrate=115200, timeout = 10)
    while(not ser.any()):
        print("No data")
        pyb.delay(100)
        pass
    setPoint = ser.readline().strip()
    KP = ser.readline()

    setPoint = int(setPoint)
    KP = float(KP)
    print(setPoint)
    print(KP)


    encoderTimer.counter(0)
    elapsed = 0
    position = 0
    t = []
    y = []

    startTime = utime.ticks_ms()
    while elapsed < 3000:
        currentTime = utime.ticks_ms()
        elapsed = currentTime - startTime
        pos = read()
        t.append(elapsed)
        y.append(pos)
        
        error = setPoint - pos
        set_duty_cycle(-(KP * error))
        pyb.delay(10)

    set_duty_cycle(0)
    u2 = pyb.UART(2, baudrate=115200, timeout = 10)
    u2.write(f'{len(y)}\r\n')
    u2.write(f'{KP}\r\n')
    for i in range(0, len(y)):  # Just some example output
        u2.write(f'{t[i]}, {y[i]}\r\n')  # The "\r\n" is end-of-line stuff
    print("sent")
    
while True:
    main()
