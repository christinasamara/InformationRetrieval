import glob
import os
import numpy as np
import nltk 
import math

nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
tokens = []
inverted_index = {}
vector_space = []
doc_length = len(os.listdir("C:\\Users\\chris\\Documents\\ceid\\7\\INFORMATION_RETRIEVAL\\InformationRetrieval\\docs30"))
vector_space = [ [] for _ in range(doc_length) ]

def append_tokens():
    for filename in glob.glob("C:\\Users\\chris\\Documents\\ceid\\7\\INFORMATION_RETRIEVAL\\InformationRetrieval\\docs30\*"):
        with open(os.path.join(os.getcwd(), filename), "r") as f:
            text = f.read()
            tokens.append(text.lower().split("\n"))

def cleanup(token_lists):
    cleaned_tokens = [[token for token in token_list if token not in stop_words and len(token) >= 4] for token_list in token_lists]
    return cleaned_tokens
        

def create_inverted_index(inverted_index):
    for i in range(len(tokens)):
        for index, token in enumerate(tokens[i]):
            if token not in inverted_index:
                inverted_index[token] = {i: [1, [index]]}
            else:
                if i in inverted_index[token]:
                    inverted_index[token][i][0] += 1
                    inverted_index[token][i][1].append(index)
                else:
                    inverted_index[token][i] = [1, [index]]


def numerator(vector_space):
    for i in range(doc_length):
        for key, value in inverted_index.items():
            if i in value:
                tf = inverted_index[key][i][0] + 1 #first element of outer list + 1
                n = len(inverted_index[key]) #length of inner list 
                vector_space[i].append(tfc(tf, n))
            else:
                vector_space[i].append(1) #not zero


def normalize(vector_space):
    N = doc_length
    for i in range(len(vector_space)):
        result = 0
        product = 0
        for key, value in inverted_index.items():
            if i in value:
                tf = inverted_index[key][i][0]
                #print(tf, n)
            else:
                tf = 1
            n = len(inverted_index[key])
            product += tf * math.log(N/n)
            result += math.sqrt(product)
        print(result)
        vector_space[i] = [num / result for num in vector_space[i]]


def tfc(tf, n):
    N = doc_length
    return tf * math.log(N/n)

append_tokens() #3219 tokens
tokens = cleanup(tokens) #1758 tokens
create_inverted_index(inverted_index)
#print(len(inverted_index))
numerator(vector_space)
normalize(vector_space)
print(vector_space)
