a = int(input())
b = int(input())
def generate(a,b):
    for x in range(a, b + 1):
        yield x**2

new_var = generate(a,b)

for x in new_var:
    print(x)
