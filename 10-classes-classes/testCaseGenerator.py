import os
from random import random
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random

def solve(n, arr):
     s = []
     f = []

     for i in range(n):
          inputArr = list(map(int, arr[i].split()))
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
     
     return len(activities)

def getTestCase():
     numberOfActivities = random.randint(4,24)
     activityTimes = []
     for i in range(numberOfActivities):
          #print(f"Activity {i+1}:")
          #activityTimes.append(input("Start time? ") + " " + input("End time? "))
          startT = random.randint(0,19)
          dur = random.randint(1,5)
          activityTimes.append(str(startT) + " " + str(startT+dur))
          
     return [str(numberOfActivities) + "\n" + "\n".join(activityTimes), str(solve(numberOfActivities, activityTimes))]

for i in range(0, 20):
     n = str(i).zfill(2)
     ioArr = getTestCase()


     inputFile = open(f'./testCases/input/input{n}.txt', 'a')
     inputFile.write(ioArr[0])
     inputFile.close()
     
     outputFile = open(f'./testCases/output/output{n}.txt', 'a')
     outputFile.write(ioArr[1])
     outputFile.close()

     print(f'Written case {n}.')

# def getTestCase():
#      numberOfActivities = int(input("Number of activities? "))
#      activityTimes = []
#      for i in range(numberOfActivities):
#           print(f"Activity {i+1}:")
#           activityTimes.append(input("Start time? ") + " " + input("End time? "))
#           
#      return [str(numberOfActivities), "\n".join(activityTimes), str(solve(numberOfActivities, activityTimes))]