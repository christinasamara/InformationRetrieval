token1 = { 'doc1' : [1, [3]], 'doc2': [2, [3,4]]}
token2 = { 'doc1' : [1, [4]], 'doc3': [2, [4,5]]}

index = { 'token1': token1, 'token2':token2}

first_element_token1_doc1 = index['token1']['doc1'][0]
print("First element for token1 and doc1:", first_element_token1_doc1)