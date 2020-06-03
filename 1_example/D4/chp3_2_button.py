#2_button.py
from gpiozero import Button
from time import sleep

button = Button(24)

while True:
    if button.is_pressed:
        print("Pressed")
    else:
        print("Released")
    sleep(1)