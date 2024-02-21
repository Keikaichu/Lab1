n = int(input())

def goback(n):
    for x in range (n,0,-1):  
        yield x
""" here n - starting point; 0 - ending point; -1 - is step of iteration"""
new_var = goback(n)
for x in new_var:
 print(x)
    