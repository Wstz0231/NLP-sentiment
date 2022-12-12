import csv


# read the idf score collected in training data
def read_idf():
    idf = {}
    filename = "idf.csv"
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 0:
                idf[row[0]] = row[1]
    return idf


# read the bookmark
def read_bookmark():
    bookmark = []
    filename = "idf.csv"
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 0:
                bookmark.append(row[0])
    return bookmark


# input the single processed tweet as a list of words, the idf dictionary and bookmark
# return a tf-idf vector
def generate_vec(tweet, idf, bookmark):
    tfidf_vec = []
    for j in range(len(bookmark)):
        word = bookmark[j]
        tf = tweet.count(word)
        tfidf = tf * idf[word]
        tfidf_vec.append(tfidf)
    return tfidf_vec
