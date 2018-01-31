import tweepy
import time
import config
import json


# Import the necessary methods from tweepy library
# reference: http://adilmoujahid.com/posts/2014/07/twitter-analytics/
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from DataAnalysis import DataAnalysis

#This is a basic listener that just prints received tweets to stdout.



class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        with open('fetched_tweets.txt','a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    stream = Stream(auth, l)

    # keywords for filter
    # keywords = ['cholesterol', 'EKG', 'aneurys' ,'angina', 'angiogenesis' ,'coronary arteries',
    #             'coronary' , 'LDL' , 'HDL' , 'bypass surgery' , 'steats' ,'high sugar level',
    #             'chest pain', 'chest pressure', 'difficulty breathing', 'heart attack', 'blood pressure', 'cardiac arrest',
    #             'Shooting left arm pain', 'arm pain', 'shooting pain', 'left arm tingling', 'shortness of breath']

    # keywords = ["cholesterol", "EKG"]

    # Bounding boxes:
    northeast = [-78.44,40.88,-66.97,47.64]
    texas = [-107.31,25.68,-93.25,36.7]
    california = [-124.63,32.44,-113.47,42.2]

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(languages=["en"],locations = texas, async=True)

    tweets_data_path = 'C:\\Users\\Dian\\PycharmProjects\\realTimeTweetsFilter\\fetched_tweets.txt'

    # dataAnalysis = DataAnalysis(tweets_data_path)
    # dataAnalysis.readFile()