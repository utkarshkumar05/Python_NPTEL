import random

def choose():
    words = ['rainbow', 'computer', 'science', 'programming', 'mathematics', 'player', 'condition', 'reverse', 'board', 'water']
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    p1=int(p1)
    p2=int(p2)
    if(p1>p2):
        print('The winner is ',p1n)
    else:
        if(p2>p1):
            print('The winner is ',p2n)
        else:
            print('You both played well, but it is a tie')
    print(p1n,' : ',p1)
    print(p2n,' : ',p2)

def play():
    p1name = input('Name of player1 = ')
    p2name = input('Name of player2 = ')
    pp1 = 0
    pp2 = 0
    turns = 0
    while(1):
        #Computer's task
        picked_word = choose()
        #Creating Question
        qn = jumble(picked_word)
        print(qn)
        #Process of Game
        #For Player 1
        if(turns%2==0):
            print(p1name,', Your Turn...')
            ans = input('What is your answer??' )
            if(ans==picked_word):
                pp1 = pp1+1
                print('Your score is: ', pp1)
            else:
                print('Better Luck next time!!, The correct answer is- ', picked_word)
            c = input('Press 1 to continue or 0 to quit: ')
            c=int(c)
            if(c==0):
                thank(p1name,p2name,pp1,pp2)
                break
        #For Player 2
        else:
            print(p2name,', Your Turn...')
            ans = input('What is your answer??' )
            if(ans==picked_word):
                pp2 = pp2+1
                print('Your score is: ', pp2)
            else:
                print('Better Luck next time!!, The correct answer is- ', picked_word)
            c = input('Press 1 to continue or 0 to quit: ')
            c=int(c)
            if(c==0):
                thank(p1name,p2name,pp1,pp2)
                break
        turns = turns+1
play()