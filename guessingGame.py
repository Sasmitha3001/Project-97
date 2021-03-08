import random
number=random.randint(1,9)
chances=5

while chances<=5:
    guess=int(input("Enter a number \t"))
    if(guess<number):
        print("Too low..try again")
    elif(guess>number):
        print("Too high...try again")
    else:
        print("Congratulations Genius!! You won!!")
        break

    chances-=1
        
    if(chances==0):
        print("Oops.. you lost :(")
        print("The number was: ",number)
        break


    

    
