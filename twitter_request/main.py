import requests
from youconfig import params, cookies, headers 
from utils import search_valid_tweet


def main() -> None: 
    #Запрос к целевому адресу
    response = requests.get(
        'https://twitter.com/i/api/graphql/eS7LO5Jy3xgmd3dbL044EA/UserTweets',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    #Ответ сервера в json
    data = response.json()
    #Преобразование в словарь и обращение к нужному ключу
    target_data = dict(data)['data']['user']['result']['timeline_v2']['timeline']['instructions'][2]['entries']

    return search_valid_tweet(target_data)
    

if __name__ == '__main__':
    #Главная точка входа
    main()