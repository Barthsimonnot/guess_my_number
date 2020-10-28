# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:04:26 2020

@author: 33637

This script will try to guess the mysterious number
prepared by guess_my_number.GuessMachine.
It's strategy is to try middle number between min and max.
It'll adapt min and max values to match GuessMachine answers.
"""


from guess_my_number import MIN, MAX, GuessMachine

if __name__ == '__main__':
    min = MIN
    max = MAX
    guess_nachine = GuessMachine()
    while True:
        attempt = int((min + max)/2)
        result = guess_nachine.guess(attempt)
        print('tried %d : %s' % (attempt, result))
        if result == 'found':
            print('Finished in %d attempts.' % guess_nachine.number_of_attempt)
            break
        elif result == 'too low':
            min = attempt + 1
        else:
            max = attempt - 1
