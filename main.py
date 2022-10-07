import os
import tweepy
import time
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.



api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")
Access_token_secret = os.getenv("Access_token_secret")
Access_token = os.getenv("Access_token")
auth = tweepy.OAuthHandler(api_key, api_secret)

auth.set_access_token(Access_token,Access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify= True)

user = api.me()

search = 'Music'

nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('tweet retweeted')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break