import math # import the math package for math.ceil()


numberOfCases = int(input()) # first line of input, number of testcases
while numberOfCases:                # while the number of remaining cases is not 0,
     n = int(input())               # take the next line of input,
     team1 = 5*(n-1)                # calculate the score for the first-placed team,
     team2 = 5*math.ceil(((n-2)/2)) # calculate the score for the second-placed team,
     maxDiff = team1-team2          # find the difference,
     print(int(maxDiff))            # print the answer,
     numberOfCases-=1               # and finally, decrement the number of cases.