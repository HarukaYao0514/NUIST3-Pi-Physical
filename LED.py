#Name:Yao Yao
#Date:31/3/25

# Import the RPi.GPIO module which is used to control the Raspberry Pi GPIO pins
import RPi.GPIO as GPIO
# Import the time module to allow us to pause the script for a specified amount of time
import time

# Set up the GPIO pin numbering scheme to BCM, which refers to the Broadcom chip-specific numbers
GPIO.setmode(GPIO.BCM)

# Disable warnings from GPIO library; these warnings can occur if you reuse a pin without cleaning up first
GPIO.setwarnings(False)

# Setup GPIO pin 18 as an output pin. This pin will be used to control the LED.
GPIO.setup(18, GPIO.OUT)

# Print "LED on" to indicate that we are about to turn the LED on
print("LED on")

# Turn the GPIO pin 18 to HIGH (3.3V), which sends power through the pin to light up the connected LED
GPIO.output(18, GPIO.HIGH)

# Wait for 1 second, keeping the LED lit during this period
time.sleep(1)

# Print "LED off" to indicate that we are about to turn the LED off
print("LED off")

# Turn the GPIO pin 18 to LOW (0V), cutting off power through the pin and turning off the LED
GPIO.output(18, GPIO.LOW)

