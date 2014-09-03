from twython import Twython
from twitter import Twitter, OAuth, TwitterHTTPError

Oauth_token =  "2774373368-6lRXLtA6161RQLCIKsNVB8iSZRP8K1uleVYwc6m"
Oauth_secret = "qR3aDBNXVvjWwUU08I4JU50Trpwi8MOL36CZhH5GIU5hD"
app_key = "dvPdyb3E8sEyvUji9Cx3WTPtO"
app_secret = "JdjdYqPgd9SYvxZ0egrc3jFHGr8gvHFpDwXwVzzFJbsQlqPd5C"
TwitterHandle = "turbotwitbot"

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

