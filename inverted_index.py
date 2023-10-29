import glob
import os
import numpy as np
import nltk 
 

nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
tokens = []
inverted_index = {}
flag = 0
doc_length = len(os.listdir("C:\\Users\\chris\\Downloads\\ir_project\\docs"))

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
            vector_space[i].append(temp[0])
        else:
            vector_space[i].append(0)

#mia synarthsh eksw na ypoloigizei ta barh

