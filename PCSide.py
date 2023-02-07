# send a KP and setpoint from the PC side
import serial
import csv
from matplotlib import pyplot as plt

'''
parameter = b'5000,.1'    # setpoint and KP

# runs step response tests by sending characters through the USB serial port to the MicroPython board
with serial.Serial('COM8', 115200, timeout=10) as s_port:
    s_port.write(parameter)  # Write bytes, not a string
print("Parameters Sent")
'''


# read the resulting data,
# plot the step response with correctly labeled axes and title.

# open the CSV file in read ('r') mode

def plotter():
    list = []
    with(serial.Serial("COM8", 115200, timeout = 10) as ser):
        expectedLength = ser.readline()
        KPused = ser.readline()
        for i in range(int(expectedLength)):
            list.append(ser.readline().split(b","))

    print(list)


if __name__ == "__main__":
    plotter()


'''
with serial.Serialopen('data.csv', 'r') as csv:
    # initialize x and y
    x_values = []
    y_values = []

    # try to read each line in the csv
    for line in csv:
        datapoint = line.strip().split(',')

        # try to convert each line into numbers
        try:
            x = float(datapoint[0])
            y = float(datapoint[1])

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
    plt.title("Position vs. Time", size=16)
    plt.xlabel("Time, t [ms]")
    plt.ylabel("Motor Position, x [encoder ticks]")
    plt.show()
'''