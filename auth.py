import tweepy
from keys import consumer, access

auth = tweepy.OAuthHandler(consumer.get("key"), consumer.get("secret"))
auth.set_access_token(access.get("token"), access.get("secret"))
twitter = tweepy.API(auth)