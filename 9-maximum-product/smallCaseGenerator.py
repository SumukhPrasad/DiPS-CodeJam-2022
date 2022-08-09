import random

s = random.randint(3,5)
ul=[random.randint(1,9) for _ in range(s)]
l = sorted(ul, reverse=1)
m = [0,0]
for x in l:
     i = m[0] > m[1]
     m[i] = m[i]*10 + x
     # Uncomment the following line to see how it's concatenating the digits.
     print(m)


print(" ".join(str(e) for e in ul))
print()
print(str(m[0] * m[1]))