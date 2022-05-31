from WebAPI.project_modules import *


def fetch_twitter_public_metrics(id='1527749317402013696'):
    url = 'https://api.twitter.com/2/tweets?ids={}&tweet.fields=public_metrics&expansions=attachments.media_keys&media.fields=public_metrics'.format(
        id)
    headers = {'Authorization': 'Bearer {}'.format(
        settings.TWITTER_BEARER_TOKEN)}

    res = requests.get(url, headers=headers)
    return(res.json())


def fetch_user(username='twitterdev'):
    url = 'https://api.twitter.com/2/users/by?usernames={}&user.fields=created_at,url,name,public_metrics,verified,username,description,pinned_tweet_id'.format(
        username)
    headers = {'Authorization': 'Bearer {}'.format(
        settings.TWITTER_BEARER_TOKEN)}
    res = requests.get(url, headers=headers)
    return res.json()


def fetch_user_recent_tweets(username='twitterdev'):
    user_details = fetch_user(username)
    if len(user_details['data']) > 0:
        create_user_data(user_details['data'][0])
        url = 'https://api.twitter.com/2/tweets/search/recent?query=from:{}&max_results=10&expansions=author_id&tweet.fields=created_at,lang,conversation_id&user.fields=created_at,entities'.format(
            username)
        headers = {'Authorization': 'Bearer {}'.format(
            settings.TWITTER_BEARER_TOKEN)}
        res = requests.get(url, headers=headers)

        twitterResData = res.json()
        for data in twitterResData['data']:
            data['metrics'] = fetch_twitter_public_metrics(data['id'])
            if len(data) > 0:
                create_twitter_data(data)
            else:
                print('Tweet data not found')
    else:
        print('User data not available')


def create_user_data(data):

    tweeter_user_detail = TwitterUsers.objects.filter(id=data['id']).exists()
    if tweeter_user_detail is False:

        TwitterUsers.objects.create(
            id=data['id'],
            url=data['url'],
            name=data['name'],
            followers_count=data['public_metrics']['followers_count'],
            following_count=data['public_metrics']['following_count'],
            tweet_count=data['public_metrics']['tweet_count'],
            listed_count=data['public_metrics']['listed_count'],
            verified=data['verified'],
            username=data['username'],
            created_at=data['created_at']
        )
    else:
        print('user_exixts')


def create_twitter_data(data):
    tweet_detail = TwwetData.objects.filter(id=data['id']).exists()
    if tweet_detail is False:

        TwwetData.objects.create(
            id=data['id'],
            author_id=data['author_id'],
            lang=data['lang'],
            retweet_count=data['metrics']['data'][0]['public_metrics']['retweet_count'],
            reply_count=data['metrics']['data'][0]['public_metrics']['reply_count'],
            like_count=data['metrics']['data'][0]['public_metrics']['like_count'],
            quote_count=data['metrics']['data'][0]['public_metrics']['quote_count'],
            text=data['metrics']['data'][0]['text'],
            # in_reply_to_user_id   = ''
            # referenced_tweets     = ''
            # mentions              = ''
        )
    else:
        print('exixts')


# fetch_user_recent_tweets()
