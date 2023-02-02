# initialize encoder and motor
# receive a setpoint
# receive a Kp

import pyb
from encoder_reader import EncoderReader
from motor_driver import MotorDriver

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

# A constructor which sets the proportional gain, initial setpoint, and other necessary parameters.

# A method run() which is called repeatedly to run the control algorithm.

# This method should accept as parameters the setpoint and measured output.

# It should return an actuation value which is sent to a motor in this lab but might be sent to another device in another instance, as this is a generic controller.

# The run() method should not contain a loop and should not print the results of its running; those things go in your main code.

# A method set_setpoint() to set the setpoint.

# A method set_Kp() to set the control gain.