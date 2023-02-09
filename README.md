# Lab 2 Memo

For this lab, we built upon our work in the last lab on encoders and motor drivers utilized on our Nucleo.
Rather than just having the encoder track position of the motor, we used the encoder in a control class to
calculate error between our desired motor position and our current one. We got both our proportional control
constant and our desired position from our PC. This was fed to our Nucleo and read into our code as data.

The Nucleo fed the code back to our pc in csv form, where our pc used matplotlib to plot the position of the
motor over time. The step response error and settling time depends greatly on our Kp. Generally a Kp of less
than one reduced settling time greatly. The higher our Kp, the faster the motor accelerated to reach the
desired position.

![High Settling Time](/Underdamped.png)

![Low Settling Time](/Underdamped2.png)

![Overdamped](/Overdamped1.png)



