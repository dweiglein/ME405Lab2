import pyb
import utime
import csv

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

encoderTimer.counter(0)
position = 0

setPoint = 5000
KP = .1

startTime = utime.ticks_ms()
print(startTime)
elapsed = 0

t = []
y = []

while elapsed < 500:
    currentTime = utime.ticks_ms()
    elapsed = currentTime - startTime

    pos = read()
    error = setPoint - pos
    set_duty_cycle(-(KP * error))
    print(error)
    
    t.append(elapsed)
    y.append(pos)
    pyb.delay(5)

set_duty_cycle(0)

file = open("step.csv", "w")
for k in y:
    file.write("{} {}\n".format(t[k], y[k]))
file.close()


with open('step.csv', 'w', newline='') as csvfile:
    data_write = csv.writer(csvfile, delimiter=',')
    data_write.writerow([t, y])

    
