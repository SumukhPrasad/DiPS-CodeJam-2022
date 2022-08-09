import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

import random
import math

for j in range(0, 20):
     ioNumber = str(j).zfill(2)

     x = random.randint(1, 10)
     k = x - random.randint(1, x)

     inputFile = open(f'./testCases/input/input{ioNumber}.txt', 'a')
     inputFile.write(str(x) + " " + str(k))
     inputFile.close()

     print((str(x) + " " + str(k)))
     r=0
     c = 1
     i = 2
     while i*i <= x:
          while x%i==0:
               x//=i
               c+=1
          i+=1
     if c >= k:
          r=1
     print(str(r))
     
     outputFile = open(f'./testCases/output/output{ioNumber}.txt', 'a')
     outputFile.write(str(r))
     outputFile.close()

     print(f'Written case {ioNumber}.')