class Infinite:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        value = self.num
        self.num += 1
        return value

obj = Infinite()

for i in obj:
    if i > 5:
        break
    print(i)
