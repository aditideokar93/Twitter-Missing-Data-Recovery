__author__ = "Aditi Deokar"

import time
import pandas as pd
import tweepy
import os
from tweepy import OAuthHandler

# authorize the app to access Twitter Streaming API
access_token = "ENTER YOUR ACCESS TOKEN"
access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
consumer_key = "ENTER YOUR CONSUMER KEY"
consumer_secret = "ENTER YOUR CONSUMER KEY SECRET"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#List of column names
COLS = ['id', 'created_at','tweet_type','source','text', 'screen_name', 'favorite_count',
        'retweet_count', 'hashtags',
        'mentions', 'media']

#path where extracted tweet links containing tweet ids are stored
path=r"D:\sns_scraper_tweet_recovery\\tweet_ids"

#path to store tweet information fetched on the basis of tweet ids passed
extracted_tweets_path=r"D:\sns_scraper_tweet_recovery\\fetched_tweets"

directory = os.listdir(path)

for file in directory:
    screenname=file.split('-')[-1] #To take out screenname from the filename eg. twitter-SpeakerPelosi
    entry = []
    fh = open(os.path.join(path, file),'r')
    for line in fh:
        tweet_id=line.split('/')[-1].strip() #Split the Link to grab the tweet_id only eg. https://twitter.com/SpeakerPelosi/status/1259647243797368833
        tweet = api.get_status(id=int(tweet_id), tweet_mode="extended")
        time.sleep(5)
        if str(tweet.created_at).split(' ')[0]>'2019-12-17':
            try:
                hashtags=tweet.entities['hashtags'][0]['text']
            except:
                hashtags=None
            try:
                user_mentions=tweet.entities['user_mentions'][0]['screen_name']
            except:
                user_mentions=None
            try:
                media=tweet.entities['media'][0]['media_url']
            except:
                media=None

            entry.append([tweet.id,tweet.created_at,'tweet',tweet.source,tweet.full_text,tweet.user.screen_name,tweet.favorite_count, tweet.retweet_count,hashtags,user_mentions,media])

            print(len(entry),screenname)
    df = pd.DataFrame(entry,columns=COLS)
    
    df.to_csv(extracted_tweets_path+'\\'+screenname+"_tweets.csv", mode='a+', columns=COLS, index=False,
                                      encoding="utf-8")
   
