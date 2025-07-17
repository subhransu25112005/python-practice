def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    


a = int(input("enter your number1: "))
b = int(input("enter your number2: "))
c = int(input("enter your number3: "))

print("The greatest of all no is",greatest(a,b,c))