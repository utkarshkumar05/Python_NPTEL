def FizzBuzz(n):
    for i  in range(1, n+1):
        if(i%3==0 and i%5==0):
            print(str(i)+"= FizzBuzz")
        else:
            if(i%3==0):
                print(str(i)+"= Fizz")
            else:
                if(i%5==0):
                    print(str(i)+"= Buzz")
                else:
                    print(str(i))
                    
FizzBuzz(51)
            