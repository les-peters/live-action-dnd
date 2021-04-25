# main

from roll import roll
from pynput import keyboard
import math

menu_selection = 0

def setMenu(new_menu):
    global menu
    global menu_selection
    menu = new_menu
    menu_selection = 0
    print(menu[menu_selection]['name'])
    return

def getModifier(ability):
    modifier = math.floor((character['abilities'][ability] - 10) / 2)
    return modifier

def checkForNat20(roll):
    if roll == 20:
        print('Natural 20!')
    return

def checkForNat1(roll):
    if roll == 1:
        print('Natural 1!')
    return

def rollSave(ability):
    d20 = roll(20)
    checkForNat20(d20)
    checkForNat1(d20)
    save = d20 + getModifier(ability)
    print('Rolled', str(save), 'on', ability, 'save')
    return save

def rollCheck(ability):
    d20 = roll(20)
    checkForNat20(d20)
    checkForNat1(d20)
    check = d20 + getModifier(ability)
    print('Rolled', str(check), 'on', ability, 'check')
    return check

def rollInit():
    d20 = roll(20)
    checkForNat20(d20)
    checkForNat1(d20)
    init = d20 + getModifier('DEX')
    print('Rolled', str(init), 'on initiative')
    return init

def on_down():
    global menu_selection
    if menu_selection == len(menu) - 1:
        menu_selection = 0
    else:
        menu_selection += 1
    print(menu[menu_selection]['name'])

def on_up():
    global menu_selection
    if menu_selection == 0:
        menu_selection = len(menu) - 1
    else:
        menu_selection -= 1
    print(menu[menu_selection]['name'])

def on_press(key):
    global menu_selection
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

range_menu = [
    { 'name': 'Return', 'func': 'setMenu(top_menu)'}
]

melee_menu = [
    { 'name': 'Return', 'func': 'setMenu(top_menu)'}
]

cast_menu = [
    { 'name': 'Return', 'func': 'setMenu(top_menu)'}
]

top_menu = [
    { 'name': 'Check', 'func': 'setMenu(check_menu)' },
    { 'name': 'Save',  'func': 'setMenu(save_menu)'  },
    { 'name': 'Melee', 'func': 'setMenu(melee_menu)' },
    { 'name': 'Range', 'func': 'setMenu(range_menu)' },
    { 'name': 'Cast',  'func': 'setMenu(cast_menu)'  },
    { 'name': 'Rest',  'func': 'setMenu(rest_menu)'  },
    { 'name': 'Init',  'func': 'rollInit()'          },
    { 'name': 'Exit',  'func': 'exit()'              }
]

menu = top_menu

character = {
    'abilities': {
        'STR': 6,
        'DEX': 18,
        'CON': 12,
        'INT': 12,
        'WIS': 9,
        'CHA': 14
    },
    'classes': [
        { 'class': 'Fighter', 'subclass': 'Arcane Archer (XGE)', 'level': 3 }
    ]
}

with keyboard.Listener(on_press=on_press, on_release=on_release, suppress=True) as l:
    l.join()