import random
def play():
    p1name = input('Name of player1 = ')
    p2name = input('Name of player2 = ')
    pp1 = 0
    pp2 = 0
    turns = 0
    while(1):
        #Conputer's task
        picked_word = choose()
        #Creating Question
        qn = jumble(picked_word)