# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities
 
n = int(input())

s = []
f = []

for i in range(n):
     inputArr = list(map(int, input().split()))
     s.append(inputArr[0])
     f.append(inputArr[1])

activities = []

# The first activity is always selected
i = 0
activities.append(i)

# Consider rest of the activities
for j in range(n):

     # If this activity has start time greater than
     # or equal to the finish time of previously
     # selected activity, then select it
     if s[j] >= f[i]:
          activities.append(j)
          i = j
 
print(len(activities))