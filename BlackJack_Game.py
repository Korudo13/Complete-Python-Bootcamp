#used for shuffling cards
import random

# Boolean used to know if hand is in play
playing = False

def chip_pool():

    amount = (100,250,500,1000)

    while True:
        try:
            bet = input('Please enter an amount to bet: 100, 250, 500, or 1000: ')

        except:
            print ('Invalid bet. Please enter 100, 250, 500 or 1000: ')
            continue

        if bet not in amount:
            continue

        else:
            print ('You betted'), bet
            break
