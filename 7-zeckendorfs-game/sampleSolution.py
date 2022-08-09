# Helper: Returns the greatest Fibonacci Number smaller than or equal to n.
def nearestSmallerEqFib(n):
     # Edge cases
     if (n == 0 or n == 1):
          return n  
     # Finds the greatest Fibonacci mumber smaller than n.
     f1, f2, f3 = 0, 1, 1
     while (f3 <= n):
          f1 = f2;
          f2 = f3;
          f3 = f1 + f2;
     return f2;
 
 
n = int(input())
result = []
while (n>0):
     # Find the greatest Fibonacci Number smaller than or equal to n
     f = nearestSmallerEqFib(n);
     # Append the fibonacci number we found
     result.append(f)
     # Reduce n
     n = n-f
result.sort()
print(" ".join(str(e) for e in result))