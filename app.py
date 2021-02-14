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

    def censor(self, tweet, tweet_words, tweet_id):
        new_msg = ""
        for word in tweet_words:
            if word not in self.new_speak:
                new_msg += " *censored* "
            else:
                new_msg += word
        api.update_status(new_msg, tweet_id)

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
            tweet_id = tweet.id
            self.censor(tweet, tweet_words, tweet_id)

        return check


team = TwitterBot('MaybeABot5', 'mattiasmattias')
team.login()
# checks if following new speak
check = team.check("MaybeABot5")
print(check)
