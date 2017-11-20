import json
import pandas as pd
import re


class DataAnalysis:
    tweets_data_path = ""

    def __init__(self, tweets_data_path):
        self.tweets_data_path = tweets_data_path

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

        texas = {"DallasCounty":{"Carrollton","Cedar Hill","Combine","Coppell","Dallas","Ferris","Garland","Glenn Heights","Grand Prairie","Grapevine","Lewisville","Mesquite","Ovilla","Richardson","Rowlett","Sachse","Seagoville","Wylie"},
                 "LubbockCounty":{"Abernathy","Idalou","Lubbock","Shallowater","Slaton","Wolfforth"}}
        for line in tweets_file:
            try:

                tweet = json.loads(line)
                if tweet['place']['place_type'] == 'city' and tweet['place']['name'] in texas['DallasCounty']:
                    tweets_data.append(tweet)

                    # tweet = json.loads(line)
                    # tweets_data.append(tweet)
            except:
                continue

        print("================================================================")
        print("The total number of tweets in the file is = %s" % (len(tweets_data)))
        print("================================================================")

        # structure the tweets data into a pandas DataFrame to simplify the data manipulation
        tweets = pd.DataFrame()

        # lang column contains the language in which the tweet was written
        # country is the country from which the tweet was sent.
        tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
        tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
        tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None,tweets_data))
        tweets['city'] = list(map(lambda tweet: tweet['place']['name'] if tweet['place'] != None else None,tweets_data))

        tweets_by_lang = tweets['lang'].value_counts()

        print("Top 5 languages in which the tweets were written : ")
        print(tweets_by_lang[:5])
        print("================================================================")

        tweets_by_country = tweets['country'].value_counts()

        print("Top 5 countries : ")
        print(tweets_by_country[:5])
        print("================================================================")

        tweets_by_city = tweets['city'].value_counts()

        print("Top 5 city : ")
        print(tweets_by_city[:5])
        print("================================================================")

        # keywords related to CVD
        listCVD = ['cholesterol', 'EKG', 'Aneurysm' ,'Angina' , 'Angiogenesis' ,'Coronary Arteries',
                   'Coronary' , 'LDL' , 'HDL' , 'bypass surgery' , 'steats' ,'high sugar level',
                   'chest pain', 'chest pressure', 'difficulty breathing', 'heart attack', 'blood pressure', 'cardiac arrest',
                   'Shooting left arm pain', 'arm pain', 'shooting pain', 'left arm tingling', 'shortness of breath']
        # keywords reference to CVD_1
        listCVD_1 = []
        # keywords reference to CVD_2
        listCVD_2 = []

        #keywords related to CVD
        itCVD = iter(listCVD)
        for x in itCVD:
            tweets[x] = tweets['text'].apply(lambda tweet: self.word_in_text(x, tweet))

        # print distribution of key words
        # keywords related to CVD
        itCVD = iter(listCVD)
        for x in itCVD:
            try:
                temp = tweets[x].value_counts()[True]
            except KeyError:
                temp = 0
            print("tweets about", x, " : ", temp)
        print("================================================================")


