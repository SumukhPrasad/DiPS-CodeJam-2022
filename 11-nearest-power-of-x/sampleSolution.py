import math

x = int(input().strip())
n = int(input().strip())

y = x**(math.ceil(math.log(n, x)))
z = x**(math.floor(math.log(n, x)))
print(y if abs(n-y)<=abs(n-z) else z)