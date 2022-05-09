"""
CPE106L_B1 - PROJECT (GAME OF WAR)

=======GROUP 3=======
CHUA, Vhal Pearson H.
FONSECA, Robne Kyle L.
GOPOLE, Khyle Matthew P.
PUNZALAN, Francine Claire T.


MAIN PYTHON SOURCE FILE
"""

from Logic import * #import from Logic.py to use Logic class

def game():
    print("========WELCOME TO GAME OF WAR========\n\nHERE ARE THE PLAYERS AND THEIR RESPECTIVE CARDS\n")
    logic = Logic(['Vhal', 'Francine', 'Robne', 'Khyle'])
    logic.deal_cards()
    logic.play_all()

def print_underline(string, line):
    print('\n{}\n{}'.format(string, line * len(string)))


if __name__ == '__main__':
    game()