# CPU Temperature example

from gpiozero import CPUTemperature
import time

cpu = CPUTemperature()

while True:
    temp_c = cpu.temperature
    temp_f = temp_c * (9.0 / 5.0) + 32.0
    print('CPU Temperature: {}F'.format(temp_f)) 
    time.sleep(1)