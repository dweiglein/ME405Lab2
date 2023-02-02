# initialize encoder and motor
# receive a setpoint
# receive a Kp

# A constructor which sets the proportional gain, initial setpoint, and other necessary parameters.

# A method run() which is called repeatedly to run the control algorithm.
# This method should accept as parameters the setpoint and measured output.

# It should return an actuation value which is sent to a motor in this lab but might be sent to another device
# in another instance, as this is a generic controller.

# The run() method should not contain a loop and should not print the results of its running; those things go
# in your main code.

# A method set_setpoint() to set the setpoint.

# A method set_Kp() to set the control gain.