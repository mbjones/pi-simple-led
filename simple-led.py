# p01-simple-led

# Copyright 2020 Matthew B. Jones
# License: Apache-2.0

# Uses one LED on GPIO 18

import RPi.GPIO as GPIO
import time
import sys

def main():
    setup()
    for i in range(1, 10):
        blink(0.25)

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)

def on():
    print("LED on")
    GPIO.output(18, GPIO.HIGH)

def off():
    print("LED off")
    GPIO.output(18, GPIO.LOW)

def blink(secs):
    print("LED blink")
    on()
    time.sleep(secs)
    off()
    time.sleep(secs)

main()
