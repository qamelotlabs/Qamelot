from WebAPI.project_modules import *
import pprint

# auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET)
# auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)

# api = tweepy.API(auth)

# user = api.get_user(screen_name='twitter')

# print(user)

client = tweepy.Client(bearer_token=settings.TWITTER_BEARER_TOKEN)

# import requests

# client = tweepy.Client( bearer_token='AAAAAAAAAAAAAAAAAAAAAFbicwEAAAAABj1KVtouWe5iLXXaKR41EWDVFcQ%3DjsJ21SeJlrVmoJeftIkjkqGOrlxx65kyYcHJycD13tgTDndphv',
#                         consumer_key=settings.TWITTER_API_KEY, 
#                         consumer_secret=settings.TWITTER_API_SECRET, 
#                         access_token=settings.TWITTER_ACCESS_TOKEN, 
#                         access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET, 
#                         return_type = requests.Response,
#                         wait_on_rate_limit=True)

# Replace with your own search query
query = 'from:BarackObama -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                tweet_fields=['created_at', 'public_metrics', 'lang', 'author_id'], expansions='author_id', 
                user_fields=['username', 'public_metrics', 'verified'], limit=5):
    pprint.pprint(tweet, width=100)