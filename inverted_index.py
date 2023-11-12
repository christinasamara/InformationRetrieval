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
def normalization(doc):
    tfi = 0
    ni = 0
    N = doc_length
    # tfi, ni enos token ka8e fora
    sum = 0
    for key, value in inverted_index.items():
        ni = len(value)
        for key2, value2 in value.items():
            if (key2 == doc):
                sum += (value2[0] * math.log(N/ni)) ** 2
    return(math.sqrt(sum))

#bgazei la8os epeidh to teleytaio keimeno einai ola 0


def tfc (token, tf, doc):
    N = doc_length
    n = find_n(token)
    #if normalization(doc)!= 0 and n!=0:
    return ( tf * math.log(N/n) ) #/ normalization(doc)
    #else:
    #    return 0.0


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
                    print(j)
                    if ( j == i ):
                        inverted_index[token][j][0] += 1
                        inverted_index[token][j][1].append(index)
                    else:
                        inverted_index[token][i] = [1, [index]]




nis()
vector_space = []



for i in range(doc_length):
    vector_space.append([])


for doc in range(doc_length):
    for key, value in inverted_index.items():
        #print(value)
        temp = value.setdefault(doc, 0)
        #print(temp)
        #print("doc",doc)

        if (isinstance(temp, list)):
            vector_space[doc].append(tfc(key, temp[0], doc))
        else:
            vector_space[doc].append(0)



    



#for key, value in inverted_index.items():
#    for key2, value2 in value.items():
#        print(key2)
#


