import pandas as pd
        
df = pd.read_csv('data2.csv', on_bad_lines = 'skip') 
df = df.head(10000)
df = df.drop(['ItemID', 'SentimentSource'], axis = 1)
positive = df.loc[df['Sentiment'] == 1]
negative = df.loc[df['Sentiment'] == 0]
positive.to_csv('positive.csv')
negative.to_csv('negative.csv')
positive.to_csv('positive.txt')
negative.to_csv('negative.txt')

