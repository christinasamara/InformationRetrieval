import glob
import os
import numpy as np
from nltk.corpus import stopwords

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
            ins_dict = {}
            ins_dict[i] = [1, [index]] 
            inverted_index[token] = ins_dict
        else:
            for j in list(inverted_index[token].keys()):
                if ( j == i ):
                    inverted_index[token][j][0] += 1
                    inverted_index[token][j][1].append(index)
                else:
                    inverted_index[token][i] = [1, [index]]

for key, value in inverted_index.items():
    print(key, ":", value)


        





