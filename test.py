token1 = { 'doc1' : [1, [3]], 'doc2': [2, [3,4]]}
token2 = { 'doc1' : [1, [4]], 'doc3': [2, [4,5]]}

import os

index = { 'token1': token1, 'token2':token2}

first_element_token1_doc1 = index['token1']['doc1'][0]

for key, value in index.items():
    temp = value.get('doc1')

    print(temp[0])
    temp2 = temp[0]
    print(temp2)

path = "C:\\Users\\chris\\Documents\\ceid\\7\\INFORMATION_RETRIEVAL\\InformationRetrieval\\docs"
name = os.path.basename(path)
print(name)
