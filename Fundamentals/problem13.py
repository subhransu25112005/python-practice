mark1 = int(input("Emter mark 1: "))
mark2 = int(input("Emter mark 2: "))
mark3 = int(input("Emter mark 3: "))
p = (100*(mark1 + mark2 + mark3))/3
if(mark1>33 and mark2>33 and mark3>33):
    if(p>=40):
        print(f"You are passed with {p:.2f} percent")
    else:
        print("You are fail\nSORRY!")
else:
    print("Fail due to less mark on each sub")