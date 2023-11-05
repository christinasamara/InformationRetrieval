import sklearn
import pandas as pd
import glob
from pathlib import Path 
from sklearn.feature_extraction.text import TfidfVectorizer



text_files = glob.glob("/Users/stella/Documents/docs/*")
text_titles = [Path(text).stem for text in text_files]
tfidf_vectorizer = TfidfVectorizer(input='filename', stop_words='english')
tfidf_vector = tfidf_vectorizer.fit_transform(text_files)
print(tfidf_vector)