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
        