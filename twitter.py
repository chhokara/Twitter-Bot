import tweepy
import time

key = "8LfgceWJmQWwmjVMLEZCp4fvn"
secret_key = "wNbCmgCbpboKBwLjbdiZr7Ugyw9bhLNVz5hYUUJU7nRVEfl5Y9"

auth = tweepy.auth.OAuthHandler(key, secret_key)

AccessKey = "872684552-W1M5j1gPwLNf7ZPYFwYu49HjjkohsZBttINuzhmE"
AccessKey_secret = "i7hVgq7furWacz4VF9UF4VsFPap5FnoxmAtXvKBWcFs2h"

auth.set_access_token(AccessKey, AccessKey_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

for follower in tweepy.Cursor(api.friends).items():
    print(follower.name)
