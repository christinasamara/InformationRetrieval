import glob
import os
import numpy as np
import nltk 
import math

mycollection = []
myqueries = []

def docs_making():
    t = open("colbert_docs.tsv", "w")
    for filename in glob.glob("C:\\Users\\chris\\Documents\\ceid\\7\\INFORMATION_RETRIEVAL\\InformationRetrieval\\docs30\*"):
        with open(os.path.join(os.getcwd(), filename), "r") as f:
            text=f.read().replace("\n", " ")
            line = os.path.basename(filename) + "\t" + text + "\n"
            t.write(line)

def queries_making():
    t = open("colbert_queries.tsv", "w")
    with open(os.path.join(os.getcwd(), "Queries_20"), "r") as f:
        text = f.read().split("\n")
        for i in range(len(text)):
            line = str(i) + "\t" + text[i] +"\n"
            t.write(line)

def collection():
    for filename in glob.glob("C:\\Users\\chris\\Documents\\ceid\\7\\INFORMATION_RETRIEVAL\\InformationRetrieval\\docs\*"):
        with open(os.path.join(os.getcwd(), filename), "r") as f:
            text=f.read().replace("\n", " ")
            line = text
            mycollection.append(line)

def queries():
    with open(os.path.join(os.getcwd(), "Queries_20"), "r") as f:
        text = f.read().split("\n")
        for i in text:
            myqueries.append(i)


docs_making()
queries_making()
collection()
queries()
print(mycollection[1])


