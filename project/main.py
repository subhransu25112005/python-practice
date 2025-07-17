# SNAKE _ WATER _ GUN
import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youdict = {"s":1,"w":-1,"g":0}
reversedict = {1:"snake",-1:"water",0:"gun"}
you = youdict[youstr]
print(f"You choose {reversedict[you]}\n Computer choose {reversedict[computer]}")


if(computer == you):
    print("DRAW")
else:
    if(computer == -1 and you == 1):
        print("YOU WIN")
    elif(computer == -1 and you == 0):
        print("YOU LOSE")
    elif(computer == 1 and you == -1):
        print("YOU LOSE")
    elif(computer == 1 and you == 0):
        print("YOU WIN")
    elif(computer == -0 and you == -1):
        print("YOU WIN")
    elif(computer == -0 and you == 1):
        print("YOU LOSE")
    else:
        print("Somrthing went wrong!!")