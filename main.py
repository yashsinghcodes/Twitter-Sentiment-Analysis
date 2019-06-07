# Importing All Important Modules
import tweepy
from textblob import TextBlob
import os
import csv

class TSA:
  def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret) # Authanticate The Conusmer Details With Twitter
    auth.set_access_token(access_token,access_token_secret) # Set the access token
    self.api = tweepy.API(auth) # Using the api

  def analysis(self,topic):
    public_tweets = self.api.search(topic) # Searching for all the public posts
    for tweet in public_tweets:
      print(tweet.text)
      analysis = TextBlob(tweet.text)
      print(analysis.sentiment) # Printing The Analysis
      print("")

  def saveToCSV(self,topic):
    with open('TSAfile.csv','w') as file:
      file_writer = csv.writer(file)
      public_tweets = self.api.search(topic)
      for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        if analysis.sentiment.polarity > 0:
          file_writer.writerow([tweet.text,'Positive']) # Saving it to the csv file
        elif analysis.sentiment.polarity < 0:
          file_writer.writerow([tweet.text,'Negative']) # Saving it to the csv file