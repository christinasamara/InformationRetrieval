import glob
import os
import numpy as np
import nltk 
import math
QUERY = 2

nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
tokens = []
inverted_index = {}
vector_space_tfc = []
vector_space_txc = []
doc_length = len(os.listdir("C:\\Users\\chris\\Documents\\ceid\\7\\INFORMATION_RETRIEVAL\\InformationRetrieval\\docs"))
vector_space_tfc = [ [] for _ in range(doc_length) ]
vector_space_txc = [ [] for _ in range(doc_length) ]
query_vector = []
listOfNames = []


def rele_docs(ele):
    s = os.listdir("C:\\Users\\chris\\Documents\\ceid\\7\\INFORMATION_RETRIEVAL\\InformationRetrieval\\docs")
    count = 0
    for i in s:
        count +=1
        if count == ele + 1:
            return i

def append_queries():
    f = open("C:\\Users\\chris\\Documents\\ceid\\7\\INFORMATION_RETRIEVAL\\InformationRetrieval\\Queries_20", "r")
    text = f.read().split('\n')
    return text


def query_weighting(text, i):
    query_vector = []
    query = text[i]
    q = query.split(" ")
    for key in inverted_index.keys():
        if key in q:
            query_vector.append(nfx(q,key))
        else:
            query_vector.append(0)
    return query_vector


def nfx(q, key):
    count = 0
    max = 1
    for term in q:
        if term == key:
            count += 1
        if (count > max):
            max = count
    
    tf = (0.5 * (count / max) + 0.5)
    nt = len(inverted_index[key])
    idf = math.log(doc_length / nt)
    return tf * idf


def append_tokens():
    for filename in glob.glob("C:\\Users\\chris\\Documents\\ceid\\7\\INFORMATION_RETRIEVAL\\InformationRetrieval\\docs\*"):
        with open(os.path.join(os.getcwd(), filename), "r") as f:
            text = f.read()
            tokens.append(text.lower().split("\n"))
    listOfNames.append(os.path.basename(filename))




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


def numerator_tfc(vector_space):
    for i in range(doc_length):
        for key, value in inverted_index.items():
            if i in value:
                tf = inverted_index[key][i][0] #first element of outer list + 1
                n = len(inverted_index[key]) #length of inner list 
                vector_space[i].append(tfc(tf, n))
            else:
                vector_space[i].append(0) #not zero


def numerator_txc(vector_space):
    for i in range(doc_length):
        for key, value in inverted_index.items():
            if i in value:
                tf = inverted_index[key][i][0] #first element of outer list + 1
                n = len(inverted_index[key]) #length of inner list 
                vector_space[i].append(txc(tf))
            else:
                vector_space[i].append(0) #not zero


def normalize_tfc(vector_space):
    N = doc_length
    for i in range(len(vector_space)):
        product = 0
        for key, value in inverted_index.items():
            if i in value:
                tf = inverted_index[key][i][0]
                #print(tf, n)
            else:
                tf = 0
            n = len(inverted_index[key])
            product += (tf * math.log(N/n) ** 2)
        vector_space[i] = [num / math.sqrt(product) for num in vector_space[i]]


def tfc(tf, n):
    N = doc_length
    return (tf) * math.log(N/n)


def txc(tf):
    return (tf) 


def normalize_txc(vector_space):
    for i in range(len(vector_space)):
        product = 0
        for key, value in inverted_index.items():
            if i in value:
                tf = inverted_index[key][i][0]
                #print(tf, n)
            else:
                tf = 0
            product += (tf ** 2) 
        vector_space[i] = [num / math.sqrt(product) for num in vector_space[i]]


def cosine(vector_space, query):
    values = []
    query_norm = np.linalg.norm(query)
    for i in range(len(vector_space)):
        inner_product = np.dot(vector_space[i], query)
        doc_norm = np.linalg.norm(vector_space[i])
        result = inner_product / (query_norm * doc_norm)
        values.append(result)

    temp = sorted(values)[-20:]
    res = []
    for ele in temp:
        res.append(values.index(ele))
    newlist = []
    for i in res:
        newlist.append(rele_docs(i))
    #print(newlist)


    

    



append_tokens()
tokens = cleanup(tokens)
create_inverted_index(inverted_index)
numerator_tfc(vector_space_tfc)
numerator_txc(vector_space_txc)
#normalize_tfc()
#normalize_txc()
text = append_queries()
query_vector = query_weighting(text, QUERY)
cosine(vector_space_txc, query_vector)

print(listOfNames)