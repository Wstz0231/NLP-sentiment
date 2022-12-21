import nltk
import numpy as np
import csv
from stop_list import closed_class_stop_words
import gc

if __name__ == "__main__":
    # read and clean the data from positive.txt and negative.txt(OF THE SAME SIZE)
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
    # create a dictionary: key being the words occurred and value being the number of positive and negative documents
    # containing the words
    count_dict = {}

    # count the number of documents
    num_document = len(data_pos_clean) + len(data_neg_clean)

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
    """
    # Calculate the delta idf score for each word
    idf_dict = {}
    for key in count_dict:
        if count_dict[key][0] != 0 and count_dict[key][1] != 0 and count_dict[key][0] != count_dict[key][1]:
            if count_dict[key][0] + count_dict[key][1] > 2:
                Nt = count_dict[key][1]
                Pt = count_dict[key][0]
                NtPt = Nt/Pt
                idf = np.log(NtPt)
                idf_dict[key] = idf
    """

    original_idf_dict = {}
    # Calculate idf score for each word
    for key in count_dict:
        Dt = count_dict[key][1] + count_dict[key][0]
        if Dt > 1:
            original_idf = np.log(num_document/Dt)
            original_idf_dict[key] = original_idf
    print(len(original_idf_dict))
    # collect garbage from memory
    gc.collect()
    # create a bookmark list for words
    bookmark = []
    for key in original_idf_dict:
        bookmark.append(key)
    # calculate delta tf-idf for each tweet
    """
    vec_pos = []
    vec_neg = []
    """
    """
    with open("delta_trained_positive.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for i in range(len(data_pos_clean)):
            tweet = data_pos_clean[i]
            tfidf_vec = []
            for j in range(len(bookmark)):
                word = bookmark[j]
                Ctd = tweet.count(word)
                if Ctd == 0:
                    tfidf = 0
                else:
                    tfidf = Ctd * idf_dict[word]
                tfidf_vec.append(tfidf)
            writer.writerow(tfidf_vec)
            gc.collect()

    with open("delta_trained_negative.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for i in range(len(data_neg_clean)):
            tweet = data_neg_clean[i]
            tfidf_vec = []
            for j in range(len(bookmark)):
                word = bookmark[j]
                Ctd = tweet.count(word)
                if Ctd == 0:
                    tfidf = 0
                else:
                    tfidf = Ctd * idf_dict[word]
                tfidf_vec.append(tfidf)
            writer.writerow(tfidf_vec)
            gc.collect()
    """

    # calculate tf-idf for each tweet
    """
    original_vec_pos = []
    original_vec_neg = []
    """
    with open("trained_positive.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for i in range(len(data_pos_clean)):
            tweet = data_pos_clean[i]
            tfidf_vec = []
            for j in range(len(bookmark)):
                word = bookmark[j]
                Ctd = tweet.count(word)
                if Ctd == 0:
                    tfidf = 0
                else:
                    tfidf = Ctd * original_idf_dict[word]
                tfidf_vec.append(tfidf)
            writer.writerow(tfidf_vec)
            gc.collect()

    with open("trained_negative.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for i in range(len(data_neg_clean)):
            tweet = data_neg_clean[i]
            tfidf_vec = []
            for j in range(len(bookmark)):
                word = bookmark[j]
                Ctd = tweet.count(word)
                if Ctd == 0:
                    tfidf = 0
                else:
                    tfidf = Ctd * original_idf_dict[word]
                tfidf_vec.append(tfidf)
            writer.writerow(tfidf_vec)
            gc.collect()

    """
    # produce output
    with open("delta_idf.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for key, value in idf_dict.items():
            writer.writerow([key, value])
    """
    """
    with open("idf.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for key, value in original_idf_dict.items():
            writer.writerow([key, value])
        
    with open("trained_negative.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for i in range(len(original_vec_neg)):
            writer.writerow(original_vec_neg[i])

    with open("trained_positive.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for i in range(len(original_vec_neg)):
            writer.writerow(original_vec_neg[i])
    """
    """
    with open("delta_trained_negative.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for i in range(len(vec_neg)):
            writer.writerow(vec_neg[i])

    with open("delta_trained_positive.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for i in range(len(vec_pos)):
            writer.writerow(vec_pos[i])
    """
