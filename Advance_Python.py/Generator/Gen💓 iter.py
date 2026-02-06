def count_up(n):
	count = 1
	while count <= n:
		yield count
		count += 1

g = count_up(5)
print(iter(g) is g)  
