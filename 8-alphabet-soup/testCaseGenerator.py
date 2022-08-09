import random
import string

import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')


def getTestCase():
     alphabet = ''.join(random.choices(string.ascii_lowercase, k=10))
     print("Alphabet:", alphabet)
     isTrue = True if int(input("Alphabet soup is true? (enter 0/1)")) == 1 else False
     str1 = alphabet
     str2 = ''.join(random.choices(alphabet, k=random.randint(10,100))) if isTrue else ''.join(random.choices(alphabet+string.ascii_lowercase, k=random.randint(10,100)))
     return [str1 + " " + str2, "true" if set([i for i in str2]).issubset(set([i for i in str1])) else "false"]

for i in range(0, 20):
     n = str(i).zfill(2)
     
     ioArr = getTestCase()


     inputFile = open(f'./testCases/input/input{n}.txt', 'a')
     inputFile.write(ioArr[0])
     inputFile.close()
     
     outputFile = open(f'./testCases/output/output{n}.txt', 'a')
     outputFile.write(ioArr[1])
     outputFile.close()

     print(f'Written case {n}.')
     print('----------------------------')
     print()

