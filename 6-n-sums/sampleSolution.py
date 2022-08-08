from itertools import *

n = int(input())
a = list(int(e) for e in input().split())

result = []

for i in range(len(a)):
     for j in permutations(a,i+1):
          if sum(j)==n:
               result.append(i+1)

print(result[0]) if len(result) else print("none")

