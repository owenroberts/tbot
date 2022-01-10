#!/usr/bin/python
# -*- coding: utf-8 -*-

print('worker working')

import tweepy
import time
import requests
import os
from nft import generate_image, get_image_data
from os import environ
from lib.cool import random_string

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

TWEET_INTERVAL = 60 * 60 # once an hour

def tweet_nft():
	
	file = get_image_data()
	filename = f"{random_string(8)}.jpg"
	# print(file)
	res = api.media_upload(filename=filename, file=file)
	print(res)
	
	api.update_status(status=message, media_ids=res.media_id)

	
	print('just posted', path)
	os.remove(path)
	time.sleep(TWEET_INTERVAL)
	tweet_nft() # need conditions here?

tweet_nft()

