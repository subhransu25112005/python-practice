temp = int(input("Enter Current Tempreature: "))
if(temp<0):
    print("Freeze")
elif(0<temp<=15):
    print("Too cold")
elif(15<temp<=27):
    print("Normal")
else:
    print("Such a Hot weather")