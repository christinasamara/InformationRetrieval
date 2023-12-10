import math
S = "AADCA"



X = [1]
Y = [1]
max = 0
newlist = X.sort()
for i in range(1, len(X)):
    distance = X[i] - X[i-1]
    if distance > max:
        max = distance

print(max)
X = X.sort