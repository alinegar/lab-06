import grovepi
from grovepi import *
from grove_rgb_lcd import *

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 4

# Connect the Grove Rotary Angle Sensor to digital port A2
# SIG,NC,VCC,GND
potentiometer = 2

grovepi.pinMode(potentiometer, "INPUT")
time.sleep(1)

# refrence voltage is 5V
adc_ref = 5

# Vcc of the grove interface is normally 5V
grove_vcc = 5

# angle of the rotary angle 
full_angle = 300 

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
        setRGB(0, 128,64)
        setText("Rotary threshold: " + degrees)

    except (IOError,TypeError) as e:
        print "Error"
    