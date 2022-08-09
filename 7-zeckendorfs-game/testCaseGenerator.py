import random

import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

def nearestSmallerEqFib(n):
     if (n == 0 or n == 1):
          return n  
     f1, f2, f3 = 0, 1, 1
     while (f3 <= n):
          f1 = f2;
          f2 = f3;
          f3 = f1 + f2;
     return f2;

for i in range(0, 20):
     n = str(i).zfill(2)
     number = random.randint(1,10**5)
     # writing input up here, because we're modifying number later.
     inputFile = open(f'./testCases/input/input{n}.txt', 'a')
     inputFile.write(str(number))
     inputFile.close()


     result = []
     while (number>0):
          f = nearestSmallerEqFib(number);
          result.append(f)
          number = number-f
     result.sort()

     
     outputFile = open(f'./testCases/output/output{n}.txt', 'a')
     outputFile.write(" ".join(str(e) for e in result))
     outputFile.close()

     print(f'Written case {n}.')

