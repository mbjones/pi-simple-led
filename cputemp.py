# CPU Temperature example

from gpiozero import LEDBarGraph, CPUTemperature
import time

cpu = CPUTemperature()
temp_c = cpu.temperature
temp_f = temp_c * 9.0 / 5.0 + 32.0
while (True):
    print('CPU Temperature: {}F'.format(temp_f)) 
    time.sleep(1)