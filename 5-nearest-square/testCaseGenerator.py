import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

import random
import math

for i in range(0, 20):
     n = str(i).zfill(2)
     s = random.randint(1,100)
     l = [random.randint(1,1000) for _ in range(s)]
     inputContent = " ".join(str(e) for e in l)
     
     arr = list(int(e) for e in inputContent.split())
     outputContent = []
     for i in range(0,len(arr)):
          sr = math.floor(math.sqrt(arr[i]))
          a = sr * sr
          b = (sr + 1) * (sr + 1)
          outputContent.append(a) if ((arr[i] - a) < (b - arr[i])) else outputContent.append(b)
     


     inputFile = open(f'./testCases/input/input{n}.txt', 'a')
     inputFile.write(inputContent)
     inputFile.close()
     
     outputFile = open(f'./testCases/output/output{n}.txt', 'a')
     outputFile.write(" ".join(str(e) for e in outputContent))
     outputFile.close()

     print(f'Written case {n}.')