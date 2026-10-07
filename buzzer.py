from machine import Pin
import time

buzzer = Pin(15, Pin.OUT)

while True:
    buzzer.value(not buzzer.value())
    time.sleep(0.5)