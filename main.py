# main

from roll import roll
from pynput import keyboard

menu = [
    'Check',
    'Save',
    'Melee',
    'Range',
    'Cast',
    'Rest',
    'Init'
]

menu_selection = 0
menu_depth = 0

a = 0

def on_down():
    global menu_selection
    if menu_selection == len(menu) - 1:
        menu_selection = 0
    else:
        menu_selection += 1
    print(menu[menu_selection])

def on_up():
    global menu_selection
    if menu_selection == 0:
        menu_selection = len(menu) - 1
    else:
        menu_selection -= 1
    print(menu[menu_selection])

def on_press(key):
    global menu_selection
    # print("Pressed {0}".format(key))
    if key == keyboard.Key.up:
        on_up()
    elif key == keyboard.Key.down:
        on_down()
    elif key == keyboard.Key.enter:
        print('selected', menu[menu_selection])

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as l:
    l.join()