n = int(input())
print(0)
def generate(n):
    for x in n:
        if(x % 2 == 0):
            yield x
        else:
            continue

new_var = generate(range (1, n + 1))

for x in new_var:
    print(x)
