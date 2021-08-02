from utils import leftingDaysForSummer
import tweepy as tw
from os import environ
#from dotenv import load_dotenv
from datetime import datetime

#load_dotenv('.env')

KEY = environ["API_KEY"]
SECRET = environ["API_SECRET_KEY"]
ACCESS_TOKEN = environ["ACCESS_TOKEN"]
ACCESS_SECRET = environ["ACCESS_TOKEN_SECRET"]

auth = tw.OAuthHandler(KEY,SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tw.API(auth)

def log (msg):
    now = datetime.now().ctime()
    print(now, " Tweeted ", msg)

def tweet ():
    lefting_days = leftingDaysForSummer()

    if lefting_days != None:
        api.update_status(lefting_days)
        log(lefting_days)