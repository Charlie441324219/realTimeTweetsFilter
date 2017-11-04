import json
import pandas as pd
import matplotlib.pyplot as plt

class dataAnalysis:
    tweets_data_path

    def __init__(self, tweets_data_path):
        self.tweets_data_path = tweets_data_path

# tweets_data_path = 'E:\STADY\expasome\realTimeTweetsFilter\fetched_tweets.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print(len(tweets_data))