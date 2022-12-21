import nltk
from stop_list import closed_class_stop_words
# import module
import pandas as pd
import numpy as np



"""
filename_pos = "positive.txt"
filename_neg = "negative.txt"
file_pos = open(filename_pos, 'r', encoding='ISO-8859-1')
file_neg = open(filename_neg, 'r', encoding='ISO-8859-1')
data_pos = file_pos.read().split("\n")
data_neg = file_neg.read().split("\n")
data_pos_clean = []
data_neg_clean = []
for i in range(len(data_pos)):
    data_process = (data_pos[i].split('\t'))[1]
    data_process2 = [x.lower() for x in nltk.word_tokenize(data_process) if x not in closed_class_stop_words and
                     x.isalpha()]
    data_pos_clean.append(data_process2)
for i in range(len(data_neg)):
    data_process = (data_neg[i].split('\t'))[1]
    data_process2 = [x.lower() for x in nltk.word_tokenize(data_process) if x not in closed_class_stop_words and
                     x.isalpha()]
    data_neg_clean.append(data_process2)
if len(data_pos_clean) > len(data_neg_clean):
    data_pos_clean = data_pos_clean[:len(data_neg_clean)]
if len(data_pos_clean) < len(data_neg_clean):
    data_neg_clean = data_neg_clean[:len(data_pos_clean)]
print(data_pos_clean[1])
"""

