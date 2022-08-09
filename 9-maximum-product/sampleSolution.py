
l = sorted(map(int, input().split()), reverse=1)
m = [0,0]
for x in l:
    i = m[0] > m[1]
    m[i] = m[i]*10 + x
    # Uncomment the following line to see how it's concatenating the digits.
    # print(m)
print(m[0] * m[1])