import tweepy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# .env file
# must --> pip install python-dotenv
import os
from dotenv import load_dotenv

load_dotenv()
# end .env import


key = os.getenv('KEY')
secret_key = os.getenv('SECRET_KEY')

AccessKey = os.getenv('ACCESSKEY')
AccessKey_secret = os.getenv('ACCESSKEY_SECRET')

auth = tweepy.OAuthHandler(key, secret_key)
auth.set_access_token(AccessKey, AccessKey_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)


class TwitterBot:

    new_speak = [
        'bigbrother',
        'bb',
        'bellyfeel',
        'blackwhite',
        'crimestop',
        'crimethink',
        'dayorder',
        'dep',
        'doubleplusgood',
        'doubleplusungood',
        'doublethink',
        'duckspeak',
        'facecrime',
        'Ficdep',
        'free',
        'fullwise',
        'goodthink',
        'goodsex',
        'goodwise',
        'Ingsoc',
        'joycamp',
        'malquoted',
        'Miniluv',
        'Minipax',
        'Minitrue',
        'Miniplenty',
        'Oldspeak',
        'oldthink',
        'ownlife',
        'plusgood',
        'plusungood',
        'Pornosec',
        'prolefeed',
        'Recdep',
        'rectify',
        'ref',
        'sec',
        'sexcrime',
        'speakwrite',
        'Teledep',
        'telescreen',
        'thinkpol',
        'unperson',
        'upsub']  # list of newspeak words

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()

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

    def check(self, user):
        # leave this for now
        check = True

        tweets = api.user_timeline(
            screen_name=user, count=200, include_rts=False, tweet_mode='extended')

        for tweet in tweets[:]:
            tweet_words = tweet.full_text.split()
            contains = any(i in tweet_words for i in self.new_speak)
            if(not contains):
                print("violation: ", tweet.full_text)
                check = False
            else:
                print("new speak: ", tweet.full_text)

        return check

    def censor(self, user, check):
        if(check == False):
            api.update_status("Big brother is watching")


team = TwitterBot('ScraperBot5', 'bigbrother16')
team.login()
# checks if following new speak
check = team.check("ScraperBot5")
print(check)
team.censor("ScraperBot5", check)
