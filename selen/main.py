from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from config import set_options
from timeout import timeout_validate
from user_script import user_script, pre_open_page
import time

def main(context=None):
    #Главная функция
    #Инициализация драйвера с опциями
    with Chrome(options=set_options()) as browser:
        #GET - запрос на главную страницу
        browser.get('https://www.nseindia.com')
        #Ожидаем появление элемента Market Data на странице
        market_data = timeout_validate(browser, el_id='link_2')
        #Перемещаем курсор к Market Data и кликаем по нему
        action_to_graph = ActionChains(browser).move_to_element(market_data).click()
        action_to_graph.perform()

        #Задержка в 1 секунду, что успел появиться dropdown
        time.sleep(1)

        #Ожидаем появление элемента Pre Open Market на странице
        pre_open_market = timeout_validate(market_data, xpath='//a[text()="Pre-Open Market"]')
        #Получаем ссылку на из атрибута элемента
        pre_open_market_href = pre_open_market.get_attribute('href')

        #Запускаем функцию для обработки этой страницы
        pre_open_page(browser, pre_open_market_href)
        
        time.sleep(1)

        #Возврат на прерыдущую страницу
        browser.back()

        time.sleep(1)
        
        #Функция пользовательского сценария
        user_script(browser)
        
if __name__ == '__main__':
    main()