strings = input().split(' ')
s1 = strings[0]
s2 = strings[1]

# issubset() method, to check if test whether every element in s2 is in s1.
string2IsASubset = set([i for i in s2]).issubset(set([i for i in s1]))

print("true" if string2IsASubset else "false")