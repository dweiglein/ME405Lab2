import pyb

enablePin = pyb.Pin.board.PA10
input1Pin = pyb.Pin.board.PB4
input2Pin = pyb.Pin.board.PB5
encoder1Pin = pyb.Pin.board.PB6
encoder2Pin = pyb.Pin.board.PB7


motorTimer = pyb.Timer(3, freq=20000)
motorpin1 = pyb.Pin(input1pin, pyb.Pin.OUT_PP)
motorpin2 = pyb.Pin(input2pin, pyb.Pin.OUT_PP)
motorch1 = timer.channel(1, pyb.Timer.PWM, pin=motorpin1)
motorch2 = timer.channel(2, pyb.Timer.PWM, pin=motorpin2)

encoderTimer = pyb.Timer(4, prescaler=0, period=0xFFFF)

set_duty_cycle(level):
        if level <= 0:
            level = -1 * level
            self.ch1.pulse_width_percent(level)
            self.ch2.pulse_width_percent(0)
        else:
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(level)
        print(f"Setting duty cycle to {level}")

motor1 = MotorDriver(enablePin, input1Pin, input2Pin, motorTimer)
    motor1.set_duty_cycle(50)