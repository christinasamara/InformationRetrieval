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
doc_length = len(os.listdir("/Users/stella/Documents/docs"))

def find_n(token):
    count = 0
    for key, value in inverted_index.items():
        if (key == token):
            count = len(value) 
    return count

def txc (token, tf):
    N = doc_length
    n = find_n(token)
    return tf 

ni = []

def nis():
    for i in inverted_index.keys():
        ni.append(find_n(i))




#normalization for each doc_vector
def paronomastistfc(doc):
    arrayparonom = []
    N = doc_length

    for key, value in inverted_index.items():
        for key2, value2 in value.items():
            if (key2 == doc):
                arrayparonom.append( (value2[0] * math.log(N/ni[i])) ** 2 )
    return sum(arrayparonom)

#bgazei la8os epeidh to teleytaio keimeno einai ola 0

def tfc (token, tf, doc):
    N = doc_length
    n = find_n(token)
    print(n, N)
    if (paronomastistfc(doc)!= 0 and n!=0):
        return ( tf * math.log(N/n) ) / paronomastistfc(doc)
    else:
        return 0.0


for filename in glob.glob("/Users/stella/Documents/docs/*"):
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


nis()
vector_space = []

for i in range(doc_length):
    vector_space.append([])

row = 0
for doc in range(doc_length):
    for key, value in inverted_index.items():
        temp = value.setdefault(row, 0)
        if (temp != 0):
            vector_space[row].append(tfc(key, temp[0], doc))
        else:
            vector_space[row].append(0)
    row += 1 


#for i in range(len(vector_space)):
#    print(vector_space[i])
