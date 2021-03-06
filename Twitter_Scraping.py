import sys,tweepy,csv,re

from textblob import TextBlob

import tkinter as tk
import requests
root=tk.Tk()
root.title("Sentimental Analyzer")
import datetime

class SentimentAnalysis:

    def __init__(self):
        self.tweets = []
        self.tweetText = []

    def DownloadData(self):
        # authenticating
        consumerKey = 'qkPJvHuKxzFZd4hbggebxR7Vp'
        consumerSecret = 'pDrBIY5ijZJFj2ENQwJqvDIf05s7OncmWko0xzxd0JcXjxBCRh'
        accessToken = '973117351557320704-JFPKQrRHkU7Iht8b46eKZkhJx8J98a6'
        accessTokenSecret = '0vWyHKiMcnPd5NhmOzaPp9TlXgPXUHkCGpvGqbivHLfKx'
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)
        #start_date = datetime.datetime(2018, 1, 1, 12, 00, 00)
        #end_date = datetime.datetime(2018, 7, 25, 20, 00, 00)
        # input for term to be searched and how many tweets to search
        searchTerm = input("Enter Keyword/Tag to search about: ")
        #67
        NoOfTerms = int(input("Enter how many tweets to search: "))
        FName = input("Enter File name to store data ")
        # searching for tweets
        #self.tweets = tweepy.Cursor(api.search, q=searchTerm +'-filter:retweets',  lang = "ur").items(NoOfTerms)
        self.tweets = tweepy.Cursor(api.search, q=searchTerm + '-filter:retweets', lang="en" ).items(NoOfTerms)
        # Open/create a file to append data to
        #csvFile = open(FName+'.csv', 'a', encoding='utf-8')
        f = open(FName+'.csv','w',encoding='utf-8')

        # Use csv writer
        #csvWriter = csv.writer(csvFile)

        # iterating through tweets fetched
        for tweet in self.tweets:
            #Append to temp so that we can store in csv later. I use encode UTF-8
            #self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            # print (tweet.text.translate(non_bmp_map))
            # #print tweet's text
            analysis = TextBlob(tweet.text)
            print(analysis,"\n")
            f.write(tweet.text+"\n" )

        # Write to csv and close csv file
            #csvWriter.writerow(analysis)

        #csvFile.close()
        f.close()


if __name__== "__main__":

    sa = SentimentAnalysis()
    sa.DownloadData()