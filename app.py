from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tweepy
import os
from dotenv import load_dotenv

# initial variables
load_dotenv()
consumer_key = os.getenv('KEY')
consumer_secret = os.getenv('SECRET_KEY')
access_token = os.getenv('ACCESSKEY')
access_token_secret = os.getenv('ACCESSKEY_SECRET')
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

class TwitterBot:
    # list of newspeak words
    new_speak = ['brother', 'bb', 'bellyfeel', 'blackwhite', 'crimestop', 'crimethink', 'dayorder', 'dep', 'doubleplusgood', 'doubleplusungood', 'doublethink', 'duckspeak', 'facecrime', 'Ficdep', 'free', 'fullwise', 'goodthink', 'goodsex', 'goodwise', 'Ingsoc', 'joycamp', 'malquoted', 'Miniluv', 'Minipax', 'Minitrue', 'Miniplenty', 'Oldspeak', 'oldthink', 'ownlife', 'plusgood', 'plusungood', 'Pornosec', 'prolefeed', 'Recdep', 'rectify', 'ref', 'sec', 'sexcrime', 'speakwrite', 'Teledep', 'telescreen', 'thinkpol', 'unperson', 'upsub']  

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()

    # login to twitter using selenium
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/?lang=en')
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    # establish tweepy connection and check if post contains new speak
    def check(self, user):
        check = True

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        
        tweets = api.user_timeline(screen_name=user, count=200, include_rts = False, tweet_mode = 'extended')
        for tweet in tweets[:]:
            tweet_words = tweet.full_text.split()
            contains = any(i in tweet_words for i in self.new_speak)
            if(not contains):
                print("violation: ", tweet.full_text)
                check = False
            else:
                print("new speak: ", tweet.full_text)
        if (not check):
            api.update_status("big brother is watching!")
        return check

    #Deletes all tweets from account
    def deleteAllTweets(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        for status in tweepy.Cursor(api.user_timeline).items():
            try:
                api.destroy_status(status.id)
                print ("Deleted:", status.id)
            except:
                print ("Failed to delete:", status.id)

team = TwitterBot(email, password)
team.login()
check = team.check(email)
print(check)
