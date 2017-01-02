import time
import random
from gpiozero import LED, Button

red = LED(2)
yellow = LED(3)
green = LED(4)
blue = LED(17)
print(red)

red_button = Button(14)
yellow_button = Button(15)
green_button = Button(18)
blue_button = Button(23)

leds = [red,yellow,green,blue]

for led in leds:
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)


while True:
    leds = [red, yellow, green, blue]
    red_button.wait_for_press()
    print("Standby for light sequence!!!")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO!!!")
    random.shuffle(leds)
    for led in leds:
        print(led)
        led.on()
        time.sleep(0.5)
        led.off()
    answer = []
    while len(answer) <4:
        time.sleep(0.3)
        if red_button.is_pressed:
            answer.append(<gpiozero.LED object on pin GPIO2, active_high=True, is_active=False>)
            red.on()
            time.sleep(0.1)
            red.off()
            print(answer)
        elif yellow_button.is_pressed:
            answer.append(<gpiozero.LED object on pin GPIO3, active_high=True, is_active=False>
")
            yellow.on()
            time.sleep(0.1)
            yellow.off()
            print(answer)
        elif green_button.is_pressed:
            answer.append(<gpiozero.LED object on pin GPIO4, active_high=True, is_active=False>)
            green.on()
            time.sleep(0.1)
            green.off()
            print(answer)
        elif blue_button.is_pressed:
            answer.append(<gpiozero.LED object on pin GPIO17, active_high=True, is_active=False>)
            blue.on()
            time.sleep(0.1)
            blue.off()
            print(answer)
    print(leds)
    print("\n")
    print(answer)
    if leds == answer:
        print("YOU WIN!!!")
        for led in leds:
            led.blink(on_time=0.2,off_time=0.2)
        time.sleep(5)
        for led in leds:
            led.off()
    else:
        red.blink(on_time=0.1,off_time=0.1)
        time.sleep(5)
        red.off()