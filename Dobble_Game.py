import string
import random
symbols = []
symbols = list(string.ascii_letters)
card1 = [0]*5
card2 = [0]*5

pos1 = random.randint(0,4)
pos2 = random.randint(0,4)  #pos1 and pos2 are positions of same symbol in card1 and card2 resp.

sameSymbol = random.choice(symbols)
symbols.remove(sameSymbol)

if (pos1 == pos2):
    card1[pos1] = sameSymbol
    card2[pos1] = sameSymbol #Assigning sameSymbol in card1 and card2 at pos1 when pos1 = pos2
    
else:
    card1[pos1] = sameSymbol
    card2[pos2] = sameSymbol
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1]) #Assigning sameSymbol to card1 and card2 at pos1 and pos2 resp.
    #And also assigning any other symbol at pos2 of card1 and pos1 of card2
    
    