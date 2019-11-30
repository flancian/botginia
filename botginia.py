#!/usr/bin/env python3

import tweepy
import secret

auth = tweepy.OAuthHandler("pagwyePax8TSOveeGYveRZ153", secret.CONSUMER_SECRET)
auth.set_access_token("1200715929707044865-6ZpORfGjD8rs3qBgwOofpNYj3ztS9j", secret.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
