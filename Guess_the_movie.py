import random

movies = ['AVENGERS', 'MATRIX', 'GRAVITY', 'MARTIAN', 'INTERSTELLER', 'INCEPTION', 'STAR WARS', 'STAR TREK', 'GUARDIANS OF THE GALAXY', 'JUSTICE LEAGUE']


def create_question(movie):
    n = len(movie)
    letters = list(movie)
    temp = []
    for i in range(n):
        if letters[i] == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn = ''.join(str(x) for x in temp)
    return qn

def is_present(letter, movie):
    

def play():
    p1name = input('Player1! Enter your name: ')
    p2name = input('Player2! Enter your name: ')
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True
    while willing:
        if turn % 2 == 0:
            # Player 1
            print(p1name, ' Your turn')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input('Please enter a letter!! ')
                if(is_present(letter, picked_movie)):
                    # unlock
                    modified_qn = unlock(modified_qn, picked_movie, ch)
                    print(modified_qn)
                    d = input(
                        'Press 1 to guess the movie or 2 to unlock another letter: ')
                    if(d == 1):
                        ans = input('Your answer is ')
                        if ans == picked_movie:
                            pp1 = pp1 + 1
                            print('Correct answer')
                            not_said = False
                            print(p1name, ' Your Score: ', pp1)
                        else:
                            print('Wrong answer, Try again!!')
                else:
                    print(letter, ' not found')
            c = input('Press 1 to continue or 0 to quit')
            if(c == 0):
                print(p1name, '! Your Score: ', pp1)
                print(p2name, '! Your Score: ', pp2)
                print('Thanks for Playing!')
                print('Have a nice day')
                willing = False
        else:
            # player2
            print(p2name, ' Your turn')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input('Please enter a letter!! ')
                if(is_present(letter, picked_movie)):
                    # unlock
                    modified_qn = unlock(modified_qn, picked_movie, ch)
                    print(modified_qn)
                    d = input(
                        'Press 1 to guess the movie or 2 to unlock another letter: ')
                    if(d == 1):
                        ans = input('Your answer is ')
                        if ans == picked_movie:
                            pp1 = pp1 + 1
                            print('Correct answer')
                            not_said = False
                            print(p1name, ' Your Score: ', pp1)
                        else:
                            print('Wrong answer, Try again!!')
                else:
                    print(letter, ' not found')
            c = input('Press 1 to continue or 0 to quit')
            if(c == 0):
                print(p1name, '! Your Score: ', pp1)
                print(p2name, '! Your Score: ', pp2)
                print('Thanks for Playing!')
                print('Have a nice day')
                willing = False
        turn = turn + 1
