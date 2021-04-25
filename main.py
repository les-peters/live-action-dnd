# main

from roll import roll
from pynput import keyboard

def setMenu(new_menu):
    global menu
    global menu_selection
    menu = new_menu
    menu_selection = 0
    print(menu[menu_selection]['name'])
    return

def rollSave(ability):
    save = roll(20)
    print('Rolled', str(save), 'on', ability, 'save')
    return save

def rollCheck(ability):
    check = roll(20)
    print('Rolled', str(check), 'on', ability, 'check')
    return check

save_menu = [
    { 'name': 'STR', 'func': 'rollSave("STR")' },
    { 'name': 'DEX', 'func': 'rollSave("DEX")' },
    { 'name': 'CON', 'func': 'rollSave("CON")' },
    { 'name': 'INT', 'func': 'rollSave("INT")' },
    { 'name': 'WIS', 'func': 'rollSave("WIS")' },
    { 'name': 'CHA', 'func': 'rollSave("CHA")' },
    { 'name': 'Return', 'func': 'setMenu(top_menu)'}
]

check_menu = [
    { 'name': 'STR', 'func': 'rollCheck("STR")' },
    { 'name': 'DEX', 'func': 'rollCheck("DEX")' },
    { 'name': 'CON', 'func': 'rollCheck("CON")' },
    { 'name': 'INT', 'func': 'rollCheck("INT")' },
    { 'name': 'WIS', 'func': 'rollCheck("WIS")'},
    { 'name': 'CHA', 'func': 'rollCheck("CHA")' },
    { 'name': 'Return', 'func': 'setMenu(top_menu)'}
]

rest_menu = [
    { 'name': 'Short' },
    { 'name': 'Long' },
    { 'name': 'Return', 'func': 'setMenu(top_menu)'}
]

top_menu = [
    { 'name': 'Check', 'func': 'setMenu(check_menu)' },
    { 'name': 'Save',  'func': 'setMenu(save_menu)' },
    { 'name': 'Melee' },
    { 'name': 'Range' },
    { 'name': 'Cast' },
    { 'name': 'Rest', 'func': 'setMenu(rest_menu)' },
    { 'name': 'Init' }
]

menu = top_menu
menu_selection = 0

def on_down():
    global menu_selection
    if menu_selection == len(menu) - 1:
        menu_selection = 0
    else:
        menu_selection += 1
    # print(type(menu[menu_selection[menu_depth]]))
    print(menu[menu_selection]['name'])

def on_up():
    global menu_selection
    if menu_selection == 0:
        menu_selection = len(menu) - 1
    else:
        menu_selection -= 1
    # print(type(menu[menu_selection[menu_depth]]))
    print(menu[menu_selection]['name'])

def on_press(key):
    global menu_selection
    # print("Pressed {0}".format(key))
    if key == keyboard.Key.up:
        on_up()
    elif key == keyboard.Key.down:
        on_down()
    elif key == keyboard.Key.left:
        eval(menu[len(menu) - 1]['func'])
    elif key == keyboard.Key.enter:
        print('selected', menu[menu_selection]['name'])
        if 'func' in menu[menu_selection].keys():
            eval(menu[menu_selection]['func'])
        else:
            print('no function defined')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release, suppress=True) as l:
    l.join()