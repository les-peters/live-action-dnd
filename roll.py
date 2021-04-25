# roll: simple dice rolling 

import random

def roll(d):
    roll = int(random.random() * d) + 1
    return roll

def adv(d):
    roll1 = roll(d)
    roll2 = roll(d)
    if roll1 > roll2:
        return roll1
    else:
        return roll2

def dis(d):
    roll1 = roll(d)
    roll2 = roll(d)
    if roll1 < roll2:
        return roll1
    else:
        return roll2

