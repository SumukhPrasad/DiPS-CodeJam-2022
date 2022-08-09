import random
import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')


for i in range(0, 20):
     n = str(i).zfill(2)
     s = random.randint(3,100)
     ul=[random.randint(1,9) for _ in range(s)]
     l = sorted(ul, reverse=1)
     m = [0,0]
     for x in l:
          i = m[0] > m[1]
          m[i] = m[i]*10 + x
          # Uncomment the following line to see how it's concatenating the digits.
          # print(m)

     inputFile = open(f'./testCases/input/input{n}.txt', 'a')
     inputFile.write(" ".join(str(e) for e in ul))
     inputFile.close()
     
     outputFile = open(f'./testCases/output/output{n}.txt', 'a')
     outputFile.write(str(m[0] * m[1]))
     outputFile.close()

     print(f'Written case {n}.')