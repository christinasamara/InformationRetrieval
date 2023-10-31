import glob
import os
import numpy as np
import nltk 
import math
 

nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
tokens = []
inverted_index = {}
flag = 0
doc_length = len(os.listdir("C:\\Users\\chris\\Downloads\\ir_project\\docs"))

def find_n(token):
    count = 0
    for key, value in inverted_index.items():
        if (value == token):
            count = len(value) 
    return count

def tfc (token, tf):
    N = doc_length
    n = find_n(token)
    return tf * math.log(N/n)

def txc (token, tf):
    N = doc_length
    n = find_n(token)
    return tf 

def normalize():
    sums = np.sum(vector_space, axis=1)
    return sums


for filename in glob.glob("C:\\Users\\chris\\Downloads\\ir_project\\docs\*"):
    with open(os.path.join(os.getcwd(), filename), "r") as f:
        text = f.read()
        tokens.append(text.lower().split("\n"))


for i in range(len(tokens)):
    for index, token in enumerate(tokens[i]):
        if token not in stop_words and len(token)>3:
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


vector_space = []

for i in range(doc_length):
    vector_space.append([])

for i in range(doc_length):
    for key, value in inverted_index.items():
        temp = value.setdefault(i, 0)
        if (temp != 0):
            vector_space[i].append(tfc(value, temp[0]))
        else:
            vector_space[i].append(0)

sums = normalize()
print(sums)
