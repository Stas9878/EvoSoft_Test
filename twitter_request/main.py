import requests
from config import params, cookies, headers
# from youconfig import params, cookies, headers


def main(): 
    response = requests.get(
        'https://twitter.com/i/api/graphql/eS7LO5Jy3xgmd3dbL044EA/UserTweets',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    data = response.json()

    target_data = dict(data)['data']['user']['result']['timeline_v2']['timeline']['instructions'][2]['entries']

    count = 0
    for tweet in target_data:
        if count == 10:
            break
        
        if 'itemContent' in tweet['content']:
            tweet_item = tweet['content']['itemContent']['tweet_results']['result']['legacy']

            if not 'retweeted_status_result' in tweet_item:
                # created_at = tweet_item['created_at']
                
                text_post = tweet_item['full_text']

                if 'http' in text_post[:5]:
                    print('Текст в посте отсутствует. Ищем дальше..\n')
                    continue
                else:
                    if 'http' in text_post:
                        http_index = text_post.index('http')
                        text =  text_post[:http_index].strip()
                    else:
                        text= text_post.strip()

                count += 1
                print(f'Пост {count} из 10\n{text}\n')

if __name__ == '__main__':
    main()