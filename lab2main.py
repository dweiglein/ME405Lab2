# initialize encoder and motor
import pyb
import utime
import csv
import serial
from encoder_reader import EncoderReader
from motor_driver import MotorDriver
from control import Control

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

# receive a setpoint
# receive a Kp

# receive a setpoint
# receive a Kp

# A constructor which sets the proportional gain, initial setpoint, and other necessary parameters.

# A method run() which is called repeatedly to run the control algorithm.

# This method should accept as parameters the setpoint and measured output.

# It should return an actuation value which is sent to a motor in this lab but might be sent to another device in another instance, as this is a generic controller.

# The run() method should not contain a loop and should not print the results of its running; those things go in your main code.

# A method set_setpoint() to set the setpoint.

# A method set_Kp() to set the control gain.

<<<<<<< HEAD
#Main Loop
if __name__ == '__main__':
    # Intake Kp and Setpt value from serial
    run_flg = 0
    param = []
    
    # Wait for serial input
    while run_flg == 0
        try:
            param = s_port.readline.split(b',')
            run_flg = 1
        except:
            run_flg = 0

    setpt = param[0]
    kp = param[1]
    
    # Initialize Controller
    control1 = Control(kp, setpt)
    
    # Set Up Encoder Values
    count = 0
    count_old = 0
    delta = 0
    time = []
    position = []
    init_time = utime.ticks_ms()
    
    # Control loop runs for 4 seconds
    while utime.ticks_ms() - init_time <= 4000:
        # Read encoder to get current position
        count = encoder1.read()
        delta = count - count_old
        if abs(delta) > 30000:
            delta = delta % 65535
        position = position + delta
        count_old = count
        
        # Run controller with current position and setpt
        psi = control1.run(position)
        
        # Update Motor
        motor1.set_duty_cycle(psi)
        
        # Append Time and Position Lists
        time_curr = utime.ticks_ms() - init_time
        time.append(time_curr)
        position.append(position)
        utime.sleep_ms(10)
    
    # Write time and position data to csv file
    file = open("step.csv", "w")
    for k in time:
        file.write("{} {}\n".format(time[k], position[k]))
    file.close()
    
    # Reset Run Flag
    run_flg = 0
