N = int(input())
numz = N 
def functiion(numz):
    for x in numz:
        yield x**2

my_nums = functiion(range (1, N + 1))

for x in my_nums:
    print(x)
