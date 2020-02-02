# pi-simple-led

Simple demo of blinking an LED in python on the Pi.

## Hardware setup

The demo was done on a Raspberry Pi 4B using a single red LED and 400 ohm resistor.

The LED is controlled via GPIO18 on the Pi.  Wire it up as: `GPIO18 -> LED -> 400ohm resistor -> GND`

## Software setup

The python script uses the GPIO python library to control the LED.  Setting the GPIO18 to its HIGH setting brings it to 3.3V, which lights the LED.  Bringing GPIO18 back to LOW turns off the LED.  The resistor limits the current flow to acceptable levels for the Pi.

