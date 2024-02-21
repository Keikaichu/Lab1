n = int(input())

def divisfourthree(n):
    for x in n:
        if(x % 3 == 0 or x % 4 == 0):
            yield x
        else:
            continue

new_var = divisfourthree(range(0,n+1))
for x in new_var:
    print(x)