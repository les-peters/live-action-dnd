# roll: simple dice rolling 

import random

def roll(d):
    roll = int(random.random() * d) + 1
    return roll