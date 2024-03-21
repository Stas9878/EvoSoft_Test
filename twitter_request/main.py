import requests
from config import params, cookies, headers



response = requests.get(
    'https://twitter.com/i/api/graphql/eS7LO5Jy3xgmd3dbL044EA/UserTweets',
    params=params,
    cookies=cookies,
    headers=headers,
)

r = response.json()

target = dict(r)['data']['user']['result']['timeline_v2']['timeline']['instructions'][2]['entries']

count = 0

for tweet in target:
    if count == 10:
        break
    if 'itemContent' in tweet['content']:
        tweet_item = tweet['content']['itemContent']['tweet_results']['result']['legacy']
        if not 'retweeted_status_result' in tweet_item:
            created_at = tweet_item['created_at']
            text_post = tweet_item['full_text']
            count += 1
            print(text_post)
            print('a')
