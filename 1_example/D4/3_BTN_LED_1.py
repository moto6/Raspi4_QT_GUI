#3_BTN_&_LED_1.py
from gpiozero import LED, Button

led = LED(18)
button = Button(24)

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()