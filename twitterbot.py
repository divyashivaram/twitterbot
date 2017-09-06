from twython import Twython
from twitter import Twitter, OAuth, TwitterHTTPError

Oauth_token =  "***"
Oauth_secret = "***"
app_key = "***"
app_secret = "***"
TwitterHandle = "***"

twitter = Twython(app_key, app_secret, Oauth_token, Oauth_secret)
def update_status(s):
    twitter.update_status(status = s)

def retweet(q, count=10):
    # twitter.retweet(id = "507254244173307904")
    search_results = twitter.search(q=q, count=count)
    try:
        for tweet in search_results["statuses"]:
            twitter.retweet(id = tweet["id_str"])
    except TwythonError as e:
            print e

# retweet(q = "Robots", count = 10)

