from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import twitter


class TwitterBot:
    new_speak = [
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
        if tweets not in TwitterBot.new_speak:
            tweets.replace(tweets)


team = TwitterBot('ScraperBot5', 'Arshdeep16')
team.login()
team.censor()
