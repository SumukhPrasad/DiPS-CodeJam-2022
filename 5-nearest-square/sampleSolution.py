import math

arr = list(int(e) for e in input().split())
outputContent = []
for i in range(0,len(arr)):
     sr = math.floor(math.sqrt(arr[i]))
     a = sr * sr
     b = (sr + 1) * (sr + 1)
     outputContent.append(a) if ((arr[i] - a) < (b - arr[i])) else outputContent.append(b)

print(" ".join(str(e) for e in outputContent))