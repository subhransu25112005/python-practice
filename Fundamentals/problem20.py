#FACTORIAL OF A GIVEN NUMBER

#while loop
n = int(input("Enter number: "))
product = 1
# if(n<=0):
#     print("Factorial is not exist f nagetive value")
# else:
#     i = 1
#     while(i<=n):
#         product *= i
#         i += 1
if(n<=0):
    print("Factorial is not exist f nagetive value")
else:
    for i in range(1,n + 1):
        product *= i
print(f"The fact of given number {n} is {product}")