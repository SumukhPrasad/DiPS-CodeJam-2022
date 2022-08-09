x,k = map(int, input().split())
c = 1
i = 2
while i*i <= x:
	while x%i==0:
		x//=i
		c+=1
	i+=1
if c >= k:
	print(1)
else:
	print(0)