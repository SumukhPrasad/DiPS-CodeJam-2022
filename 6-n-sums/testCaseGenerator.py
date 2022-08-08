from itertools import *
import random

import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

for i in range(0, 20):
     n = str(i).zfill(2)
     number = random.randint(2,100)
     a = [random.randint(1,number-1) for _ in range(10)]

     result = []

     for i in range(len(a)):
          for j in permutations(a,i+1):
               if sum(j)==number:
                    result.append(i+1)

     inputFile = open(f'./testCases/input/input{n}.txt', 'a')
     inputFile.write(str(number) + "\n" + " ".join(str(e) for e in a))
     inputFile.close()
     
     outputFile = open(f'./testCases/output/output{n}.txt', 'a')
     outputFile.write(str(result[0]) if len(result) else "none")
     outputFile.close()

     print(f'Written case {n}.')