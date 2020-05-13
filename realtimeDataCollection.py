__author__="Aditi Deokar"

import os
import tweepy
from datetime import datetime
import datetime
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from http.client import IncompleteRead

# authorize the app to access Twitter Streaming API
access_token = "ENTER YOUR ACCESS TOKEN"
access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
consumer_key = "ENTER YOUR CONSUMER KEY"
consumer_secret = "ENTER YOUR CONSUMER KEY SECRET"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

path="K:\Forex_tweet_extraction\\Tweets_extraction\\Politicians_JSONS\\Politicians_realtime_democrat_json"

#politicians user ids since filter(follow=) takes user ids only
politicians=['1089859058', '43910797', '117501995', '109071031', '249787913', '171598736']


class FileWriteListener(StreamListener):

    def __init__(self):
        super(StreamListener, self).__init__()
        self.save_file = open(path+'\\tweets_'+str(datetime.date.today())+'.json','a+')
        self.tweets = []

    def on_data(self, tweet):
        self.tweets.append(json.loads(tweet))
        self.save_file.write(str(tweet))
        # print("str(tweet)")
        print("captured")

    def on_error(self, status):
        print(status)
        return True


def start_stream():

    while True:
        print("Twitter API Connection opened")
        try:
            twitter_stream = Stream(auth, FileWriteListener())
            # Here you can filter the stream by:
            #    - keywords/hashtags
            #    - users(as shown) Note: Pass userids instead of twitter handle names to the filter method
            twitter_stream.filter(follow=politicians)

        except IncompleteRead:
            print("Incomplete tweet")
            continue
        except Exception as e:
            print("Error:", e)
            continue
        finally:
            print("Twitter API Connection closed")

if __name__ == '__main__':
    start_stream()


