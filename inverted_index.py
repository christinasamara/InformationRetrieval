import glob
import os
import numpy as np

tokens = []
inverted_index = {}
flag = 0
for filename in glob.glob("C:\\Users\\chris\\Downloads\\ir_project\\docs\*"):
    with open(os.path.join(os.getcwd(), filename), "r") as f:
        text = f.read()
        tokens.append(text.lower().split("\n"))
       

for i in range(len(tokens)):
    for index, token in enumerate(tokens[i]):
        if token not in inverted_index:
            inverted_index[token] = [i, 1, [index]]
        else:
            if inverted_index[token][0] == i

        inverted_index[token][1] +=1
        inverted_index[token][2].append(index)


        





