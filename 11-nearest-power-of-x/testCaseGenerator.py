import io
import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

import random
import math

for i in range(0, 20):
     ioNumber = str(i).zfill(2)

     x = random.randint(2, 50)
     n = random.randint(1, 1000)

     y = x**(math.ceil(math.log(n, x)))
     z = x**(math.floor(math.log(n, x)))

     inputFile = open(f'./testCases/input/input{ioNumber}.txt', 'a')
     inputFile.write(str(x) + "\n" + str(n))
     inputFile.close()
     
     outputFile = open(f'./testCases/output/output{ioNumber}.txt', 'a')
     outputFile.write(str(y if abs(n-y)<=abs(n-z) else z))
     outputFile.close()

     print(f'Written case {ioNumber}.')