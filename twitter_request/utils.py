def format_text(text_post):
    if 'http' in text_post[:5]:
        print('Текст в посте отсутствует. Ищем дальше..\n')
        return

    if 'http' in text_post:
        http_index = text_post.index('http')
        text =  text_post[:http_index].strip()
    else:
        text = text_post.strip()

    return text


def search_valid_tweet(target_data):
        count = 0
        for tweet in target_data:
            if count == 10:
                break
            
            if 'itemContent' in tweet['content']:
                tweet_item = tweet['content']['itemContent']['tweet_results']['result']['legacy']
                
                text_post = tweet_item['full_text']

                text = format_text(text_post)

                if text:
                    count += 1
                    print(f'Пост {count} из 10\n{text}\n')
