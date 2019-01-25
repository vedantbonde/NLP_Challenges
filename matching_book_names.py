# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:45:53 2019

@author: vedant bonde
"""

import numpy as np
import fileinput
import re
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

## First, we start by reading the input
N = int(input()) # finding the number of books
titles = [input() for i in range(N)] #  Now we do the reading of the book titles
input() # the separator
descr = [input() for i in range(N)]
#print(N)
#print(len(titles))

corpus = titles + descr

## Text Cleaning

# 1) Make all letters lowercase

corpus = [x.lower() for x in corpus]

# 2) Remove all non-alphanumeric characters (e.g. punctuation marks); also collapses multiple spaces that are created upon the removal of a character
corpus = [re.sub('[^A-Za-z0-9]+', ' ', x) for x in corpus]
#print(corpus)

## Text Vectorization 
bag_of_words = CountVectorizer(max_df=0.3, stop_words='english', binary=True)
tfidf_dist = TfidfVectorizer(max_df=0.3, norm ='l2', stop_words='english')

bag_matrix = bag_of_words.fit_transform(corpus)
tfidf_matrix = tfidf_dist.fit_transform(corpus)

## Cosine Similarity: 
# For each book description, determine which book title (document) it is most similar to
for r in tfidf_matrix[N:, :]: # for each description 
    q = cosine_similarity(r, tfidf_matrix[0:N, :])
    best_matching_title_index = np.argmax(q) + 1
    print(best_matching_title_index)
    