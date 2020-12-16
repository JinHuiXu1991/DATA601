import random
import numpy as np

def dice_simulate_fair(n):  
    fair_dice = random.randint(1,6)
    return fair_dice

def dice_simulate_biased(n):
    dice_list = [1,2,3,4,5,6]
    biased_dice = np.random.choice(dice_list, 1, p=[0.15, 0.15, 0.15, 0.15, 0.15, 0.25])[0]
    return biased_dice