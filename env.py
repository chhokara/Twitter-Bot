#.env file
#must --> pip install python-dotenv
import os
from dotenv import load_dotenv

load_dotenv()
#end .env import


key = os.getenv('KEY')
secret_key = os.getenv('SECRET_KEY')

AccessKey = os.getenv('ACCESSKEY')
AccessKey_secret = os.getenv('ACCESSKEY_SECRET')