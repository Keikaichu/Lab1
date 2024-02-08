#ex 1
def ounces(x):
    print( x * 28.3495231)


a = float(input())
ounces(a)

#ex 2
def Celcium(x):
    c = (5 / 9) * (x - 32)
    print(c)

x = int(input())
Celcium(x)

#ex3
def solve(num_heads, num_legs):
  chickens = (2 * num_legs - 4 * num_heads) // 2
  rabbits = num_heads - chickens

  if chickens >= 0 and rabbits >= 0:
    return chickens, rabbits
  else:
    return None

num_heads = int(input())
num_legs = int(input())

solution = solve(num_heads, num_legs)

if solution is None:
  print("No solution found.")
else:
  chickens, rabbits = solution
  print(f"Number of chickens: {chickens}")
  print(f"Number of rabbits: {rabbits}")

#ex4

def is_prime(n):
    if n > 1:
        for i in range(2 , int(n/2) + 1):
            if (n % i) == 0:
                return False
        else: return True
    else: return False

x = (1,3,4,5,16,34,13,19,5,31,70)
l = int(len(x))
for i in range(l):
    if(is_prime(x[i])):
        print(x[i])
        
#ex5
from itertools import permutations 

s = str(input())
perm = permutations(s)

for i in list(perm):
  print(i)

#ex6

def rev(s):
  rev_s = s[::-1]
  print(rev_s)


s = str(input())
rev(s)

#ex7
def has33(x):
  l = len(x)
  for i in range(l - 1):
    if x[i] == 3 and x[i+1] == 3:
      return True
  return False
    
  
  
x1 = ([1,3,3])
x2 = ([1,2,3,4])
x3 = ([3,1,3])

print(has33(x1))
print(has33(x2))
print(has33(x3))

#ex8
def spy_game(n):
  for i in range(len(n) - 1):
    if n[i] == 0 and n[i+1] == 0 and n[i+2] == 7:
      return True
  return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#ex9
import math

def vol(r):
  v = 4/3*(math.pi)*(r**3)
  print(v)
  
r = int(input())
vol(r)

#ex10
list1 = [100,100,20,30,400,45,45,100,20,5]

res = []

for item in list1:
  if item not in res:
    res.append(item)
    
for item in res:
  print(item)
  
#ex11
def isPalindrome(s):
  if s == s[::-1]:
    return True
  return False
    
s = str(input())
if isPalindrome(s):
  print("Yes")
else: 
  print("No")
  
#ex12
def histogram(x):
  for i in range(len(x)):
    print("*" * x[i])
    
x = ([4,9,7])
histogram(x)

#ex13
import random
print(random.randrange(1,20))
    
#ex14
import random

arr = []
for i in range(10):
  arr.insert(i,random.randrange(1,10))
r = random.randrange(1,10)

def has(x):
  

  for i in range(len(x) - 1):
    if x[i] == r and x[i + 1] == r:
      True
    else:
      False
      
if has(arr):
  print("This random number: " + str(r) + " occurs twice in a row in this random list: " + str(arr))
else:
  print("This random number: " + str(r) + " doesn't occur twice in a row in this random list: " + str(arr))