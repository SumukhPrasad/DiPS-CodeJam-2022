import random
import math


s = random.randint(1,5)
l = [random.randint(1,1000) for _ in range(s)]
inputContent = " ".join(str(e) for e in l)

arr = list(int(e) for e in inputContent.split())
outputContent = []
for i in range(0,len(arr)):
     sr = math.floor(math.sqrt(arr[i]))
     a = sr * sr
     b = (sr + 1) * (sr + 1)
     outputContent.append(a) if ((arr[i] - a) < (b - arr[i])) else outputContent.append(b)

print(inputContent)
print()
print(" ".join(str(e) for e in outputContent))