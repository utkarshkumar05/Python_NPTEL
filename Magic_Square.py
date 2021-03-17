def magic_square(n):
    
    magicSquare = []
    
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
        
    i = n/2
    j = n-1
    
    num = n*n
    count = 1
    