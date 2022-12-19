import tweepy ,os

CK = os.environ.get("TWITTER_API_CONSUMER_KEY")
CS = os.environ.get("TWITTER_API_CONSUMER_SECRET")
AT = os.environ.get("TWITTER_API_ACCESS_TOKEN_KEY")
AS = os.environ.get("TWITTER_API_ACCESS_TOKEN_SECRET")


auth = tweepy.OAuthHandler(CK,CS)

auth.set_access_token(AT,AS)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print('-------------------------')
#     print(tweet.text)

# for tweet in tweepy.Cursor(api.search_tweets, q='幸せ').items(10):
#     print(tweet.user.name+"さんが",tweet.text,"と呟きました")


# TWEET_TEXT = "こんばんはああああ！"

# api.update_status(TWEET_TEXT)
