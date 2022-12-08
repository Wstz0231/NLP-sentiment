import nltk
import string
import numpy as np
import csv
from stop_list import closed_class_stop_words

if __name__ == "__main__":
    # read and clean the data from positive.txt and negative.txt(OF THE SAME SIZE)
    filename_pos = "positive.txt"
    filename_neg = "negative.txt"
    file_pos = open(filename_pos, 'r', encoding="utf-8")
    file_neg = open(filename_neg, 'r', encoding="utf-8")
    data_pos = file_pos.read().split('\n')
    data_neg = file_neg.read().split('\n')
    if len(data_pos) != len(data_neg):
        print("Error!")
    data_pos_clean = []
    data_neg_clean = []
    for i in range(len(data_pos)):
        tweet_pos = data_pos[i].translate(str.maketrans('', '', string.punctuation))
        tweet_neg = data_neg[i].translate(str.maketrans('', '', string.punctuation))
        tokenized_tweet_pos = [x.lower() for x in nltk.word_tokenize(tweet_pos) if x not in closed_class_stop_words]
        tokenized_tweet_neg = [x.lower() for x in nltk.word_tokenize(tweet_neg) if x not in closed_class_stop_words]
        data_pos_clean.append(tokenized_tweet_pos)
        data_neg_clean.append(tokenized_tweet_neg)
    # create a dictionary: key being the words occurred and value being the number of positive and negative documents
    # containing the words
    count_dict = {}
    if len(data_pos_clean) != len(data_neg_clean):
        print("Error")
    for i in range(len(data_pos_clean)):
        tweet_pos = data_pos_clean[i]
        tweet_neg = data_neg_clean[i]

        for j in range(len(tweet_pos)):
            pos_word = tweet_pos[j]
            if pos_word not in count_dict:
                count_dict[pos_word] = [0, 0]

        for k in range(len(tweet_neg)):
            neg_word = tweet_neg[k]
            if neg_word not in count_dict:
                count_dict[neg_word] = [0, 0]

    for i in range(len(data_pos_clean)):
        tweet_pos = data_pos_clean[i]
        tweet_neg = data_neg_clean[i]

        for key in count_dict:
            if key in tweet_pos:
                count_dict[key][0] += 1
            if key in tweet_neg:
                count_dict[key][1] += 1
    # Calculate the idf score for each word
    idf_dict = {}
    for key in count_dict:
        if count_dict[key][0] != 0 and count_dict[key][1] != 0:
            Nt = count_dict[key][1]
            Pt = count_dict[key][0]
            NtPt = Nt/Pt
            idf = np.log(NtPt)
            idf_dict[key] = idf
    # create a bookmark list for words
    bookmark = []
    for key in idf_dict:
        bookmark.append(key)
    # calculate tf-idf for each tweet
    vec_pos = []
    vec_neg = []
    for i in range(len(data_pos_clean)):
        tweet = data_pos_clean[i]
        tfidf_vec = []
        for j in range(len(bookmark)):
            word = bookmark[j]
            Ctd = tweet.count(word)
            tfidf = Ctd * idf_dict[word]
            tfidf_vec.append(tfidf)
        vec_pos.append(tfidf_vec)

    for i in range(len(data_neg_clean)):
        tweet = data_neg_clean[i]
        tfidf_vec = []
        for j in range(len(bookmark)):
            word = bookmark[j]
            Ctd = tweet.count(word)
            tfidf = Ctd * idf_dict[word]
            tfidf_vec.append(tfidf)
        vec_neg.append(tfidf_vec)
    # produce output
    with open("idf.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for key, value in idf_dict.items():
            writer.writerow([key, value])

    with open("trained_negative.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for i in range(len(vec_neg)):
            writer.writerow(vec_neg[i])

    with open("trained_positive.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for i in range(len(vec_pos)):
            writer.writerow(vec_pos[i])

