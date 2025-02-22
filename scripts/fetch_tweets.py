import tweepy

auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_SECRET")
api = tweepy.API(auth)

tweets = api.search_tweets(q="AWS", lang="en", count=5)

for tweet in tweets:
    print(tweet.text)
