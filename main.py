import tweepy
import time
import config
import json


# Import the necessary methods from tweepy library
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

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['python'], async=True)

tweets_data_path = 'E:\\STADY\\expasome\\realTimeTweetsFilter\\fetched_tweets.txt'

dataAnalysis = DataAnalysis(tweets_data_path)
dataAnalysis.readFile()