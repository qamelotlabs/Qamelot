from WebAPI.project_modules import *

def fetch_twitter_public_metrics(id = '1527749317402013696'):
    url = 'https://api.twitter.com/2/tweets?ids={}&tweet.fields=public_metrics&expansions=attachments.media_keys&media.fields=public_metrics'.format(id)
    headers = {'Authorization': 'Bearer {}'.format(settings.TWITTER_BEARER_TOKEN)}

    res = requests.get(url, headers=headers)
    print('result: ', res.json())

def fetch_user(username = 'twitterdev'):
    url = 'https://api.twitter.com/labs/2/users/by?usernames={}&user.fields=created_at,description,pinned_tweet_id'.format(username)
    headers = {'Authorization': 'Bearer {}'.format(settings.TWITTER_BEARER_TOKEN)}

    res = requests.get(url, headers=headers)
    print('result: ', res.json())

def fetch_user_recent_tweets(username = 'twitterdev'):
    url = 'https://api.twitter.com/2/tweets/search/recent?query=from:{}&max_results=10&expansions=author_id&tweet.fields=created_at,lang,conversation_id&user.fields=created_at,entities'.format(username)
    headers = {'Authorization': 'Bearer {}'.format(settings.TWITTER_BEARER_TOKEN)}

    res = requests.get(url, headers=headers)
    # print('result: ', res.json())

    twitterResData = res.json()
    # print(twitterResData['data'])
    for data in twitterResData['data']:
        print(data['created_at'])
        fetch_twitter_public_metrics(data['id'])

fetch_user_recent_tweets()