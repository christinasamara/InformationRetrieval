import glob
import os
import numpy as np
import nltk 
import math

nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
tokens = []
inverted_index = {}
doc_length = len(os.listdir("C:\\Users\\chris\\Documents\\ceid\\7\\INFORMATION_RETRIEVAL\\InformationRetrieval\\docs"))

def append_tokens():
    for filename in glob.glob("C:\\Users\\chris\\Documents\\ceid\\7\\INFORMATION_RETRIEVAL\\InformationRetrieval\\docs\*"):
        with open(os.path.join(os.getcwd(), filename), "r") as f:
            text = f.read()
            tokens.append(text.lower().split("\n"))

def cleanup(token_lists):
    cleaned_tokens = [[token for token in token_list if token not in stop_words and len(token) >= 4] for token_list in token_lists]
    return cleaned_tokens
        

def create_inverted_index(inverted_index):
    for i in range(len(tokens)):
        for index, token in enumerate(tokens[i]):
            if token not in stop_words and len(token) > 3:
                if token not in inverted_index:
                    inverted_index[token] = {i: [1, [index]]}
                else:
                    if i in inverted_index[token]:
                        inverted_index[token][i][0] += 1
                        inverted_index[token][i][1].append(index)
                    else:
                        inverted_index[token][i] = [1, [index]]


append_tokens() #3219 tokens
tokens = cleanup(tokens) #1758 tokens
create_inverted_index(inverted_index)
print(len(inverted_index))