import unittest
import tweepy
import requests
import json
import twitter_info


consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret

#set up the authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

CACHE_DICTION = {};
search_text = "University of Michigan"
unique_identifier = "twitter_{}".format(search_text) 

if unique_identifier in CACHE_DICTION:
	twitter_results = CACHE_DICTION[unique_identifier]
else:
	twitter_results = api.search(q=search_text) # get it from the internet
	CACHE_DICTION[unique_identifier] = twitter_results
	
	

print(CACHE_DICTION[unique_identifier])