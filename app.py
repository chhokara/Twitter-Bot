from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tweepy


class TwitterBot:
    new_speak = [
        'brother',
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

    def censor(self):
        bot = self.bot
        tweets = bot.find_element_by_class_name(
            "css-1dbjc4n").text

    def check(self, user):
        # leave this for now 
        check = True
        consumer_key = "1dWixBjnCsHRpVXkNQKJChbrs"
        consumer_secret = "TD8nsomVhCJM1cvJk7TbIia94V4y8KTksgWeLa4HqYfUjF7MxY"
        access_token = "1360738471388741635-TfDNeRcIVEFahuaLxOvNEENajcJJPH"
        access_token_secret = "vLAcZKM9vl8f5ForXgDemfWSbb2gfVv5n0isldfH3ifRM"
        
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

team = TwitterBot('MaybeABot5', 'mattiasmattias')
team.login()
team.censor()
# checks if following new speak
check = team.check("MaybeABot5")
print(check)
