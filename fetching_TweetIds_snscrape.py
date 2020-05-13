__author__ = "Aditi Doekar"

import os

politicians=['SpeakerPelosi','SenatorMenendez','SenStabenow','SenatorTester','SenWhitehouse','SenatorDurbin']
for speaker in politicians:
    os.system("snscrape --max-results 700 twitter-user "+speaker+"  >D:\sns_scraper_tweet_recovery\\tweet_ids\\twitter-"+speaker)

"""
sample filename= twitter-SpeakerPelosi.txt
This file will contain the html links to the tweets fetched. eg.https://twitter.com/SpeakerPelosi/status/1259595056564047876
"""
