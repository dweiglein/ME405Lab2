# send a KP and setpoint from the PC side
import serial
import csv
from matplotlib import pyplot as plt



setpoint = input("Enter setpoint: ")
KP = input("Enter KP: ")

# converting to string
str_setpoint = str(setpoint)
byte_setpoint = str_setpoint.encode()
str_KP = str(KP)
byte_KP = str_KP.encode()


# runs step response tests by sending characters through the USB serial port to the MicroPython board
with serial.Serial('COM8', 115200, timeout=10) as s_port:
    s_port.write(byte_setpoint)
    s_port.write(b'\r\n')
    s_port.write(byte_KP)
print("Parameters Sent")



# read the resulting data,
# plot the step response with correctly labeled axes and title.

# open the CSV file in read ('r') mode

def plotter():
    x_values = []
    y_values = []
    with(serial.Serial("COM8", 115200, timeout = 10) as ser):
        expectedLength = ser.readline().strip()
        KPused = ser.readline().strip()
        for i in range(int(expectedLength)):
            newline = ser.readline().strip().split(b',')
            # try to convert each line into numbers
            try:
                x = float(newline[0])
                y = float(newline[1])

                # only if both numbers are converted do they append
                x_values.append(x)
                y_values.append(y)
            except ValueError:
                pass

    # plot, label, and display - fun stuff found at:
    plt.plot(x_values, y_values, 'k')
    plt.minorticks_on()
    plt.axhline(y=0, color='black', linewidth = .3)
    plt.axvline(x=0, color='black', linewidth = .3)
    plt.title("Position vs. Time for KP " + str(float(KPused)), size=16)
    plt.xlabel("Time, t [ms]")
    plt.ylabel("Motor Position, x [encoder ticks]")
    plt.show()

if __name__ == "__main__":
    plotter()