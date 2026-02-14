num = {1, 2, 3, 4}

print(hasattr(num , '__iter__'))   #iterable
print(hasattr(num , '__next__'))

it = iter(num)
print(hasattr(it ,'__iter__'))     #iterator
print(hasattr(it , '__next__'))