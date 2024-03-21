
#Функция для форматирования текста
def format_text(text_post: str) -> str | None:
    #Если http есть в начале строки, то текст отсутствует
    if 'http' in text_post[:5]:
        print('Текст в посте отсутствует. Ищем дальше..\n')
        return
    
    #Если http есть в тексте, то обрезаем строку до ссылки
    #Если нет, то возвращаем строку
    if 'http' in text_post:
        #Находим индекс с которого начинается ссылка
        http_index = text_post.index('http')
        #Обрезаем строку
        text =  text_post[:http_index].strip()
    
    else:
        text = text_post.strip()

    return text


#Поиск текста твитов
def search_valid_tweet(target_data: list[dict]) -> None:
        #Щётчик кол-ва постов
        count = 0
        #Обход списка словарей с данными твитов
        for tweet in target_data:
            #Выбираем нужно кол-во твитов для прекращения работы программы
            if count == 10:
                break
            #Проверяем, есть ли контент в посте
            if 'itemContent' in tweet['content']:
                #Объект поста
                tweet_item = tweet['content']['itemContent']['tweet_results']['result']['legacy']
                #Полный текст поста
                text_post = tweet_item['full_text']
                #Форматируем текст
                text = format_text(text_post)

                #Если вернули строку а не None, то делаем принт и увеличиваем счётчик
                if text:
                    count += 1
                    print(f'Пост {count} из 10\n{text}\n')
