from pynput.mouse import Button, Controller
import time

time.sleep(4)
mouse = Controller()

#Refocus Window
mouse.position = (1959, 235)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(2)

time.sleep(1)

#Refocus Window no.2
mouse.position = (1696, 457)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(2)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(0.5)
mouse.press(Button.left)
mouse.release(Button.left)

#Pressing Play Button
mouse.position = (504, 243)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(1)

#Selecting Solo Q
mouse.position = (560, 1079)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(1)

#Pressing OK
mouse.position = (1121, 1208)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(2)

#Selecting ADC
mouse.position = (1042, 853)
mouse.press(Button.left)
time.sleep(0.5)
mouse.move(300, -300)
mouse.release(Button.left)
time.sleep(0.2)

#Selecting Mid
mouse.position = (1182, 852)
mouse.press(Button.left)
time.sleep(0.5)
mouse.move(0, -200)
mouse.release(Button.left)
time.sleep(1)

#Pressing Find Match
mouse.position = (1117, 1209)
mouse.press(Button.left)
mouse.release(Button.left)