n = int(input()) # Line 1 input
m = int(input()) # Line 2 input

# Helper functions:
def fillXOfArray(arr, n):
    newArr = arr;
    for i in range(len(arr[n])):
        arr[n][i] = 1
    return newArr
        
def fillYOfArray(arr, n):
    newArr = arr;
    for i in range(len(arr)):
        arr[i][n] = 1
    return newArr

arrx = []
arry = []
for i in range(0, m):
     m_input = list(map(int, input().split(" ")))
     arrx.append(int(m_input[0])) # x inputs from stdin
     arry.append(int(m_input[1])) # y inputs from stdin

grid = [[None] * n for i in range(n)] # Grid of size n

for i in range(len(arrx)):  # for each value of x,y (arrx and arry are the same length)
     grid = fillXOfArray(grid, arrx[i]-1) # fill that row with 1 (denoting lighted stalls)
     grid = fillYOfArray(grid, arry[i]-1) # fill that column with 1 (denoting lighted stalls)

sumOfOccurences = 0;
for i in range(len(grid)):
     sumOfOccurences+=sum(x is None for x in grid[i]) # Find the number of stalls that are not lit

print(sumOfOccurences)