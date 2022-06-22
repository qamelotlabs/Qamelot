from Qamelot.project_modules import *
from datetime import date

def fetch_twitter_public_metrics(id='1527749317402013696'):
    url = '{}tweets?ids={}&tweet.fields=public_metrics&expansions=attachments.media_keys&media.fields=public_metrics'.format(settings.TWITER_API_URL, id)
    headers = {'Authorization': 'Bearer {}'.format(
        settings.TWITTER_BEARER_TOKEN)}

    res = requests.get(url, headers=headers)
    return(res.json())


def fetch_user(username='twitterdev'):
    url = '{}users/by?usernames={}&user.fields=created_at,url,name,public_metrics,verified,username,description,pinned_tweet_id'.format(settings.TWITER_API_URL, username)
    headers = {'Authorization': 'Bearer {}'.format(
        settings.TWITTER_BEARER_TOKEN)}
    res = requests.get(url, headers=headers)
    return res.json()


def fetch_user_recent_tweets(usernames='twitterdev', keyword='Platform'):
    objs = NFTCollection.objects.all()
    influencer_names = ''
    for o in objs:
        print('collection_name: ', o.collectionName) 
        keyword = o.collectionName
        url = '{}tweets/search/recent?query={} from:{}&max_results=10&expansions=author_id&tweet.fields=created_at,lang,conversation_id,in_reply_to_user_id,referenced_tweets&user.fields=created_at,entities'.format(settings.TWITER_API_URL, keyword, usernames)
        headers = {'Authorization': 'Bearer {}'.format(
            settings.TWITTER_BEARER_TOKEN)}
        res = requests.get(url, headers=headers)
        twitterResData = res.json()
        if 'data' in twitterResData:
            for data in twitterResData['data']:
                data['metrics'] = fetch_twitter_public_metrics(data['id'])
                data['collection_id'] = o.id
                if len(data) > 0:
                    print(data)
                    create_twitter_data(data)
                else:
                    print('Tweet data not found1')
            collection_seed_status = CollectionSeedStatus.objects.create(
                collection_id=o.id,
                status=True,
                created_at=str(date.today())
            )
        else:
            print('Tweet data not found2')

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
            created_at=data['created_at'],
        )
    else:
        print('user_exixts')
        TwitterUsers.objects.filter(id__exact=data['id']).update(
            url=data['url'],
            name=data['name'],
            followers_count=data['public_metrics']['followers_count'],
            following_count=data['public_metrics']['following_count'],
            tweet_count=data['public_metrics']['tweet_count'],
            listed_count=data['public_metrics']['listed_count'],
            verified=data['verified'],
            username=data['username'],
        )


def create_twitter_data(data):
    tweet_detail = TweetData.objects.filter(id=data['id']).exists()
    if tweet_detail is False:
        if 'data' in data['metrics']:
            tweetDetail = TweetData.objects.create(
                id=data['id'],
                author_id=data['author_id'],
                lang=data['lang'],
                retweet_count=data['metrics']['data'][0]['public_metrics']['retweet_count'],
                reply_count=data['metrics']['data'][0]['public_metrics']['reply_count'],
                like_count=data['metrics']['data'][0]['public_metrics']['like_count'],
                quote_count=data['metrics']['data'][0]['public_metrics']['quote_count'],
                twitter_text=data['metrics']['data'][0]['text'],
                collection_id=data['collection_id']
            )
            if 'in_reply_to_user_id' in data:
                TweetData.objects.filter(id__exact=tweetDetail.id).update(
                    in_reply_to_user_id=data['in_reply_to_user_id']
                )
            if 'referenced_tweets' in data:
                TweetData.objects.filter(id__exact=tweetDetail.id).update(
                    referenced_tweets=data['referenced_tweets']
                )
        else:
            print('Twitter public metrics not available.')
    else:
        print('Twitter data updating.')
        if 'data' in data['metrics']:
            TweetData.objects.filter(id__exact=data['id']).update(
                    author_id=data['author_id'],
                    lang=data['lang'],
                    retweet_count=data['metrics']['data'][0]['public_metrics']['retweet_count'],
                    reply_count=data['metrics']['data'][0]['public_metrics']['reply_count'],
                    like_count=data['metrics']['data'][0]['public_metrics']['like_count'],
                    quote_count=data['metrics']['data'][0]['public_metrics']['quote_count'],
                    twitter_text=data['metrics']['data'][0]['text'],
                    collection_id=data['collection_id']
                )

            if 'in_reply_to_user_id' in data:
                TweetData.objects.filter(id__exact=data['id']).update(
                    in_reply_to_user_id=data['in_reply_to_user_id']
                )
            if 'referenced_tweets' in data:
                TweetData.objects.filter(id__exact=data['id']).update(
                    referenced_tweets=data['referenced_tweets']
                )
        else:
            print('Twitter public metrics not available.')


def fetch_influencers():
    objs = NftInfluencers.objects.all()
    influencer_names = ''
    for o in objs:
        print('name: ', o.name)
        user_details = fetch_user(o.name)
        if 'data' in user_details:
            if len(user_details['data']) > 0:
                create_user_data(user_details['data'][0])
                influencer_names += o.name+' OR '
    influencer_names = influencer_names[:-4]
    print('----'+influencer_names)
    fetch_user_recent_tweets(influencer_names)    

# fetch_influencers()