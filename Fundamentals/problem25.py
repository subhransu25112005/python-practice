def ftc(f):
    return 5 * (f-32)/9

f = int(input("Enter current temp in f: "))
c = ftc(f)
print(f"current temp in celsious is {c:.2f}")


