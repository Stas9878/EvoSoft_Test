from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

def rss_app(browser, url):
    #Функция для обращения к сервису rss.app

    #GET - запрос на страницу поиска по ссылке
    browser.get('https://rss.app/rss-feed/create-twitter-rss-feed')

    #Находим input
    inpt = browser.find_element(By.ID, ':r0:')
    #Вставляем в input ссылку на страницу Илона
    inpt.send_keys(url)
    #Отправляем форму, и переходим на новый url
    button_accept = browser.find_element(By.ID, 'provider-submit').click()
    
    #Ждём загрузки элементов на странице
    feed = WebDriverWait(browser, timeout=20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'tss-k2zsea-FeedCardOverview-content'))
    )

    #Возвращаем browser для дальнейшей работы с этой страницей
    return browser

    
def main(browser):
    #Функция для работы со страницей постов Илона
    
    posts = []
    #Делаем scroll на странице, пока нам не будут 
    #доступны минимум 10 постов
    while len(posts) < 10:
        #Делаем Scroll
        ac_scroll = ActionChains(browser).scroll_by_amount(delta_x=0, delta_y=2000)
        ac_scroll.perform()
        #Обновляем список постов
        posts = posts = browser.find_elements(By.XPATH, '//a[@class="MuiTypography-root MuiTypography-h3 tss-1h8hsy-FeedCardOverview-title mui-1ti1707-Typography-fontWeightBold"]')
    
    #Обход 10 последних постов и печать их текста
    for num, post in enumerate(posts[:10], 1):
        text = post.text        
        print(f'Пост #{num}:\n\t{text if text else "Текст отсутствует"}\n')
    
if __name__ == '__main__':
    #Экземпляр опций для драйвера
    options = ChromeOptions()
    #Добавили опцию для запуска без окна
    options.add_argument("--headless")

    #Инициализация драйвера
    with Chrome(options=options) as browser:
        #Ссылка на профиль нужного пользователя
        user_url = 'https://twitter.com/elonmusk'
        #Получения результата функции rss_app
        new_browser = rss_app(browser, user_url)
        #Запуск основной функции
        main(browser)