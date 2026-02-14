def gen_nums():
    for i in range(1, 1_000_000):
        yield i

g = gen_nums()
print(next(g))  
print(next(g)) 

