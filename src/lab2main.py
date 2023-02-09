"""!
@file lab2main.py

This file is Lab 2 for ME 405. The goal of this exercise was to control a 12V
DC motor system as a servo system with a proportional controller. The motor is
connected to an external power supply and a STM32 PWM output. The built-in encoder
provides position feedback and uses STM-32 timers. At the beginning of the
program sequence, controller parameters are sent through UART serial communication
to the STM32, initializing the control algorithm.

The proportional controller is the most simple closed-loop controller, using
just one variable (Kp, the controller constant), to direcetly impact the amount
of "effort" that the motor applies. The "effort" applied to the motor is a duty
cycle percentage. To find the required duty cycle, the algorithm calculates the
difference between the setpoint (goal) and the actual position and multiplies it
by the proportional controller constant. A higher error implies a higher corrective
effort, while a lower error applied a lower corrective effort. Eventually, the
error becomes negligible and no further correction is needed.

This program uses 3 classes: MotorDriver, EncoderReader, and Control. After defining
the pins and starting the timer channels, the control loop waits for motor parameters.
Once the controller parameters (Kp and setpt) are received from the PC. The encoder
reads the position, which is used by the controller to calculate the required duty
cycle, which is applied to the motor. This loop runs for 3 seconds.

@author Tom Taylor
@author Jonathan Fraser
@author Dylan Weiglein

@date   2022-02-08
"""

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
    

