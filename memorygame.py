import time
import random
from gpiozero import LED, Button

red_pin = LED(2)
yellow_pin = LED(3)
green_pin = LED(4)
blue_pin = LED(17)

red_button = Button(14)
yellow_button = Button(15)
green_button = Button(18)
blue_button = Button(23)

def lights(colour,duration):
    if colour == "red":
        red_pin.on()
        time.sleep(duration)
        red_pin.off()
        time.sleep(duration)
    elif colour == "yellow":
        yellow_pin.on()
        time.sleep(duration)
        yellow_pin.off()
        time.sleep(duration)
    elif colour == "green":
        green_pin.on()
        time.sleep(duration)
        green_pin.off()
        time.sleep(duration)
    elif colour == "blue":
        blue_pin.on()
        time.sleep(duration)
        blue_pin.off()
        time.sleep(duration)

leds = ["red","yellow","green","blue"]

for led in leds:
    lights(led,0.3)

while True:
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
        #print(led)
        lights(led,0.2)
    answer = []
    while len(answer) <4:
        time.sleep(0.3)
        if red_button.is_pressed:
            answer.append("red")
            lights("red",0.1)
            print(answer)
        elif yellow_button.is_pressed:
            answer.append("yellow")
            lights("yellow",0.1)
            print(answer)
        elif green_button.is_pressed:
            answer.append("green")
            lights("green",0.1)
            print(answer)
        elif blue_button.is_pressed:
            answer.append("blue")
            lights("blue",0.1)
            print(answer)
    if leds == answer:
        print("YOU WIN!!!")
        for blink in range(10):
            lights("red",0.1)
            lights("yellow",0.1)
            lights("green",0.1)
            lights("blue",0.1)
    else:
        print("YOU LOSE!!!")
        for blink in range(10):
            lights("red",0.1)
