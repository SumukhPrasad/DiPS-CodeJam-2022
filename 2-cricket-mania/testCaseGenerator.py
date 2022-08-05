import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

import random
import math

for i in range(0, 20):
     n = str(i).zfill(2)

     inputContent = ""
     outputContent = ""

     t = random.randint(1,50)
     inputArr = []
     outArr = []
     for j in range(t):
          r = random.randint(2,50)
          inputArr.append(r)
          outArr.append((5 * (r - 1)) - (5 * math.ceil((r - 2) / 2)))
     
     
     inputContent = str(t) + "\n" + ("\n".join(str(e) for e in inputArr))
     outputContent = "\n".join(str(e) for e in outArr)


     inputFile = open(f'./testCases/input/input{n}.txt', 'a')
     inputFile.write(inputContent)
     inputFile.close()
     
     outputFile = open(f'./testCases/output/output{n}.txt', 'a')
     outputFile.write(outputContent)
     outputFile.close()

     print(f'Written case {n}.')