from tweet import tweet
from time import time,sleep
from tweepy.error import TweepError

#:)

DAY_IN_SECONDS = 86400.0

if __name__ == '__main__':
    starttime = time()
    while True:
        try:
            tweet()   
            sleep(DAY_IN_SECONDS - ((time() - starttime) % DAY_IN_SECONDS))
        except TweepError:
            # This exception ocurrs if the same tweet is already tweeted
            # So we just let the day pass
            print("Taking the day off beacuse a tweet with that body is already posted")
            sleep(DAY_IN_SECONDS - ((time() - starttime) % DAY_IN_SECONDS))
