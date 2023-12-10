import glob
import os
import numpy as np
import nltk 
import math
results = []
relevant_docs = []
K = 20

def initialization(file):
    f = open(file, "r")
    lines = f.read().split("\n")
    for line in lines:
        results.append(line.split(" "))

def open_relevants(file):
    f = open(file, "r")
    text = f.read().split("\n")
    for t in text:
        relevant_docs.append(t)

def precisions(QUERY):
    count_relevant = 1
    sum_precisions = 0
    for rank, doc in enumerate(results[QUERY], 1):
        if doc in relevant_docs[QUERY]:
            precision = count_relevant / rank 
            sum_precisions += precision
            count_relevant += 1

    average_precision = sum_precisions / count_relevant
    return average_precision

open_relevants("Relevant_20")
f = open("Queries_20")

# initialization("tfc_results.txt")
# for query in range(len(f.read().split("\n"))):
#     print(precisions(query))

initialization("txc_results.txt")
for query in range(len(f.read().split("\n"))):
    print(precisions(query))






