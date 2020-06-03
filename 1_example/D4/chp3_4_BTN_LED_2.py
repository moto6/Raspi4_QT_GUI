#4_BTN_&_LED_2.py
from gpiozero import LED, Button

led = LED(18)
button = Button(24)

while True:
    button.wait_for_press()
    led.on()
    button.wait_for_release()
    led.off()