import grovepi
from grovepi import *
from grove_rgb_lcd import *
import time


# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 4


# Connect the Grove Rotary Angle Sensor to digital port A2
# SIG,NC,VCC,GND
potentiometer = 2


grovepi.pinMode(potentiometer, "INPUT")
grovepi.set_bus("RPI_1")
time.sleep(1)


# refrence voltage is 5V
adc_ref = 5


# Vcc of the grove interface is normally 5V
grove_vcc = 5


# angle of the rotary angle
full_angle = 300

setRGB(69, 75, 27)
while True:
   try:
       # Read sensor value from Rotary
       threshold = grovepi.analogRead(potentiometer)
       # Calculate voltage
       voltage = round((float)(threshold) * adc_ref / 1023, 2)
       # Calculate rotation in degrees
       degrees = round((voltage*full_angle) / grove_vcc, 2)
       # Read distance value from Ultrasonic
       distance = grovepi.ultrasonicRead(ultrasonic_ranger)
       #setText_norefresh("Threshold: {}{}".format(str(threshold), " OBJ PRES" if distance < threshold else ""), 0)
       #setText_norefresh("Distance: {}".format(str(distance)), 1)
       if(distance < threshold):
           #Red screen because there is an object present
           setRGB(136, 8, 8)
           setText_norefresh(str(threshold)+"cm OBJ PRES\n" + str(distance)+"cm")
           #setText("Distance: " + str(distance))
       else:
           #Green screen becuase there is no object present
           setRGB(69, 75, 27)
           setText_norefresh(str(threshold)+"cm           \n" + str(distance)+"cm")
           #setText("Distance: " + str(distance))

       time.sleep(0.1)


   except KeyboardInterrupt:
       setText("")
       break