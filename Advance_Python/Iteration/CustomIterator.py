class Count:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        value = self.start
        self.start += 1
        return value

obj = Count(1, 100)

for i in obj:
    print(i)
