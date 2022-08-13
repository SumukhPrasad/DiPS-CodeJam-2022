import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

def delannoy(m, n):
     if m==0 or n==0:
          return 1
     
     return delannoy(m-1, n) + delannoy(m-1, n-1) + delannoy(m, n-1)

for i in range(0, 10):
     n = str(i).zfill(2)

     inputFile = open(f'./testCases/input/input{n}.txt', 'a')
     inputFile.write(str(i))
     inputFile.close()
     
     outputFile = open(f'./testCases/output/output{n}.txt', 'a')
     outputFile.write(str(delannoy(i+1, i+1)))
     outputFile.close()

     print(f'Written case {n}.')