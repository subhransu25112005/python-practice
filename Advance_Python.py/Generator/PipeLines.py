def numbers(n):
    for i in range(1, n + 1):
        yield i

def even_filter(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

def square(nums):
    for num in nums:
        yield num * num


pipeline = square(even_filter(numbers(25)))

for result in pipeline:
    print(result)
