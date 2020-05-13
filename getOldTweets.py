__author__ = "Aditi Deokar"

"""
The Python code below makes use of GetOldTweets3 Package to collect older tweets
"""
import time
import pandas as pd
import tweepy
from tweepy import OAuthHandler
import GetOldTweets3 as got

# authorize the app to access Twitter Streaming API
access_token = "ENTER YOUR ACCESS TOKEN"
access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
consumer_key = "ENTER YOUR CONSUMER KEY"
consumer_secret = "ENTER YOUR CONSUMER KEY SECRET"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#list of column names
COLS = ['id', 'created_at','original_text', 'screen_name', 'author_id',
        'replies', 'retweet_count', 'to','hashtags',
        'user_mentions', 'urls']

path=r"D:\Older_tweets_data"

politicians=['SenatorMenendez','SenStabenow','SenatorTester','SenWhitehouse','SenatorDurbin']

#Function to fetch the tweet object, grab the information and write into a .csv file
for screenname in politicians:
    entry = []
    tweetCriteria = got.manager.TweetCriteria().setUsername(screenname)\
                                               .setSince("2019-12-18")\
                                               .setUntil("2020-01-01")\
                                               .setMaxTweets(1000)\
                                               .setEmoji("unicode")
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    for twt in tweet:
        entry.append([twt.id,twt.formatted_date,twt.text,twt.username,twt.author_id,twt.replies,twt.retweets,twt.to,twt.hashtags,twt.mentions,twt.urls])
    print(len(entry),screenname)
    df = pd.DataFrame(entry,columns=COLS)
    # print(df.head())
    df.to_csv(path+'\\'+screenname+"_tweets.csv", mode='a+', columns=COLS, index=False,
                                      encoding="utf-8")
    time.sleep(3)


