# main

from roll import roll
from pynput import keyboard

menu = {
    '0': { 'name': 'Check' },
    '1': { 'name': 'Save' },
    '2': { 'name': 'Melee' },
    '3': { 'name': 'Range' },
    '4': { 'name': 'Cast' },
    '5': { 'name': 'Rest' },
    '6': { 'name': 'Init' }
}

menu_selection = [ '0' ]
menu_depth = 0

def on_down():
    global menu_selection
    if menu_selection[menu_depth] == str(len(menu) - 1):
        menu_selection[menu_depth] = '0'
    else:
        menu_selection[menu_depth] = str(int(menu_selection[menu_depth]) + 1)
    # print(type(menu[menu_selection[menu_depth]]))
    print(menu[menu_selection[menu_depth]]['name'])

def on_up():
    global menu_selection
    if menu_selection[menu_depth] == '0':
        menu_selection[menu_depth] = str(len(menu) - 1)
    else:
        menu_selection[menu_depth] = str(int(menu_selection[menu_depth]) - 1)
    # print(type(menu[menu_selection[menu_depth]]))
    print(menu[menu_selection[menu_depth]]['name'])

def on_press(key):
    global menu_selection
    # print("Pressed {0}".format(key))
    if key == keyboard.Key.up:
        on_up()
    elif key == keyboard.Key.down:
        on_down()
    elif key == keyboard.Key.enter:
        print('selected', menu[menu_selection[menu_depth]]['name'])

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release, suppress=True) as l:
    l.join()