#3_7
from gpiozero import *

def pressed():
    print("TICK")

def released():
    print("TOCK")


btn = Button(24)
btn.when_pressed = pressed
btn.when_released = released
#btn.close()