def infinite_counter():
    i = 1
    while True:
        yield i
        i += 1

g = infinite_counter()

for num in g:
    if num > 5:
        break
    print(num)
