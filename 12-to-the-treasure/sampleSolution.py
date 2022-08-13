n = int(input())

def delannoy(m, n):
     if m==0 or n==0:
          return 1
     
     return delannoy(m-1, n) + delannoy(m-1, n-1) + delannoy(m, n-1)

print(delannoy(n, n))