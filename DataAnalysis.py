import json
import pandas as pd
import matplotlib.pyplot as plt
import re


class DataAnalysis:
    tweets_data_path = ""

    def __init__(self, tweets_data_path):
        self.tweets_data_path = tweets_data_path

    # tweets_data_path = 'E:\STADY\expasome\realTimeTweetsFilter\fetched_tweets.txt'

    def word_in_text(self, word, text):
        word = word.lower()
        text = text.lower()
        match = re.search(word, text)
        if match:
            return True
        return False

    def readFile(self):
        tweets_data = []
        tweets_file = open(self.tweets_data_path, "r")
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tweets_data.append(tweet)
            except:
                continue


        print("The total number of lines in the file is = %s" % (len(tweets_data)))

        # structure the tweets data into a pandas DataFrame to simplify the data manipulation
        tweets = pd.DataFrame()

        # lang column contains the language in which the tweet was written
        # country is the country from which the tweet was sent.
        tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
        tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
        tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None,
                                tweets_data)

        #top 5 languages in which the tweets were written, and the second the Top 5 countries from which the tweets were sent.
        tweets_by_lang = tweets['lang'].value_counts()

        fig, ax = plt.subplots()
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=10)
        ax.set_xlabel('Languages', fontsize=15)
        ax.set_ylabel('Number of tweets' , fontsize=15)
        ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
        tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

        # top 5 countries
        tweets_by_country = tweets['country'].value_counts()

        fig, ax = plt.subplots()
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=10)
        ax.set_xlabel('Countries', fontsize=15)
        ax.set_ylabel('Number of tweets', fontsize=15)
        ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
        tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

        tweets['python'] = tweets['text'].apply(lambda tweet: self.word_in_text('python', tweet))
        tweets['javascript'] = tweets['text'].apply(lambda tweet: self.word_in_text('javascript', tweet))
        tweets['ruby'] = tweets['text'].apply(lambda tweet: self.word_in_text('ruby', tweet))

        # print distribution of key words
        print(tweets['python'].value_counts()[True])
        print(tweets['javascript'].value_counts()[True])
        print(tweets['ruby'].value_counts()[True])

        # draw distribution of key words
        prg_langs = ['python', 'javascript', 'ruby']
        tweets_by_prg_lang = [tweets['python'].value_counts()[True], tweets['javascript'].value_counts()[True],
                              tweets['ruby'].value_counts()[True]]

        x_pos = list(range(len(prg_langs)))
        width = 0.8
        fig, ax = plt.subplots()
        plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

        # Setting axis labels and ticks
        ax.set_ylabel('Number of tweets', fontsize=15)
        ax.set_title('Ranking: python vs. javascript vs. ruby (Raw data)', fontsize=10, fontweight='bold')
        ax.set_xticks([p + 0.4 * width for p in x_pos])
        ax.set_xticklabels(prg_langs)
        plt.grid()
