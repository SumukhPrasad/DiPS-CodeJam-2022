# Helper
def isPrime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

arr = []

# Take input
for _ in range(3):
     arr.append(list(map(int, input().rstrip().split())))

arrayOfPrimes = []
for subarray in arr:
     for n in subarray:
          if isPrime(n): arrayOfPrimes.append(n) # Add all primes to a list

if len(arrayOfPrimes) == 0:
     print("none")
else:
     min = arrayOfPrimes[0]
     for i in range(1, len(arrayOfPrimes)):
          if arrayOfPrimes[i] < min:
               min = arrayOfPrimes[i]
     print(min)