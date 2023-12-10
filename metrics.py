import glob
import os
import numpy as np
import nltk 
import math
results = []
relevant_docs = []
K = 20

def initialization(file):
    results = [] 
    f = open(file, "r")
    lines = f.read().split("\n")
    for line in lines:
        results.append(line.split(" "))
    return results

def open_relevants(file):
    f = open(file, "r")
    text = f.read().split("\n")
    for t in text:
        relevant_docs.append(t)

def precisions(QUERY, results):
    count_relevant = 1
    sum_precisions = 0
    for rank, doc in enumerate(results[QUERY], 1):
        if doc in relevant_docs[QUERY]:
            precision = count_relevant / rank 
            sum_precisions += precision
            count_relevant += 1

    average_precision = sum_precisions / count_relevant
    return average_precision


def ap_results_tfc(file, query_file):
    f = open(file, "w")
    q = open(query_file, "r")
    results = initialization("tfc_results.txt")
    for query in range(len(q.read().split("\n"))):
        f.write(str(precisions(query, results)))
        f.write("\n")


def ap_results_txc(file, query_file):
    f = open(file, "w")
    q = open(query_file, "r")
    results = initialization("txc_results.txt")
    for query in range(len(q.read().split("\n"))):
        f.write(str(precisions(query, results)))
        f.write("\n")


def ap_results_colbert(file, query_file):
    f = open(file, "w")
    q = open(query_file, "r")
    results = initialization("colbert_results.txt")
    for query in range(len(q.read().split("\n"))):
        f.write(str(precisions(query, results)))
        f.write("\n")

open_relevants("Relevant_20")
ap_results_tfc("ap_results_tfc.txt", "Queries_20")
ap_results_txc("ap_results_txc.txt", "Queries_20")
ap_results_colbert("ap_results_colbert.txt", "Queries_20")

# initialization("txc_results.txt")
# for query in range(len(f.read().split("\n"))):
#     print(precisions(query))







