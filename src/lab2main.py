# initialize encoder and motor
import pyb
import utime
from encoder_reader import EncoderReader
from motor_driver import MotorDriver
from control import Control
from pyb import UART

# motor pins
enablePin = pyb.Pin.board.PA10
input1Pin = pyb.Pin.board.PB4
input2Pin = pyb.Pin.board.PB5

# encoder pins
encoder1Pin = pyb.Pin.board.PB6
encoder2Pin = pyb.Pin.board.PB7

# set up timers
motorTimer = pyb.Timer(3, freq=20000)
encoderTimer = pyb.Timer(4, prescaler=0, period=0xFFFF)

# initialize motor and timer
motor1 = MotorDriver(enablePin, input1Pin, input2Pin, motorTimer)
encoder1 = EncoderReader(encoder1Pin, encoder2Pin, 0, 0)

# Initialize ser
ser = pyb.UART(2, baudrate=115200, timeout = 10)

# A constructor which sets the proportional gain, initial setpoint, and other necessary parameters.

# A method run() which is called repeatedly to run the control algorithm.

# This method should accept as parameters the setpoint and measured output.

# It should return an actuation value which is sent to a motor in this lab but might be sent to another device in another instance, as this is a generic controller.

# The run() method should not contain a loop and should not print the results of its running; those things go in your main code.

# A method set_setpoint() to set the setpoint.

# A method set_Kp() to set the control gain.

def main():
    #Receive a setpoint and kp
    ser = pyb.UART(2, baudrate=115200, timeout = 10)
    while(not ser.any()):
        # print("No data")
        pyb.delay(100)
        pass
    setpt = ser.readline().strip()
    kp = ser.readline()

    setpt = int(setpt)
    kp = float(kp)
#     print(setpt)
#     print(kp)
    
    # Initialize Controller
    control1 = Control(kp, setpt)
    control1.set_setpoint(setpt)
    control1.set_Kp(kp)
    
    # Set up Encoder Values
    encoderTimer.counter(0)
    elapsed = 0
    position = 0
    t = []
    y = []
    
    # Control loop runs for 3 seconds
    startTime = utime.ticks_ms()
    while elapsed < 3000:
        currentTime = utime.ticks_ms()
        elapsed = currentTime - startTime
        pos = encoder1.read()
        t.append(elapsed)
        y.append(pos)
        
        psi = control1.run(pos)
        motor1.set_duty_cycle(psi)
        pyb.delay(10)
        
        # Append Time and Position Lists
#         time_curr = utime.ticks_ms() - init_time
#         time.append(time_curr)
#         position.append(pos)
#         utime.sleep_ms(10)
    
    motor1.set_duty_cycle(0)
    print("STOP")
    u2 = pyb.UART(2, baudrate=115200, timeout = 10)
    u2.write(f'{len(y)}\r\n')
    print(len(y))
    u2.write(f'{kp}\r\n')
    print(kp)
    for i in range(0, len(y)):  # Just some example output
        u2.write(f'{t[i]}, {y[i]}\r\n')  # The "\r\n" is end-of-line stuff
    print("sent")    

#Main Loop
while __name__ == '__main__':
    main()
    

