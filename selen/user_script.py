from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from timeout import timeout_validate, timeout_option
from writer_csv import writer_in_csv
import time

def pre_open_page(browser, href):
    #Функция для обработки страницы Pre-Open Market
    
    #GET-запрос к целевой странице
    browser.get(href)

    #Ожидаем появления таблицы
    page = timeout_validate(browser, el_id='livePreTable')

    #Находим тело таблицы
    tbody = browser.find_element(By.TAG_NAME, 'tbody')

    time.sleep(2)

    #Находим строки таблицы
    tr_table = tbody.find_elements(By.TAG_NAME, 'tr')[:-1]

    data = []
    #Обход строк таблицы
    for tr in tr_table:
        #Scroll до каждого элемента
        action_to_tr = ActionChains(browser).scroll_to_element(tr)
        action_to_tr.perform()

        #Название ценных бумаг
        name = tr.find_element(By.CLASS_NAME, 'symbol-word-break')
        #Итоговая цена
        final_price = tr.find_element(By.CSS_SELECTOR, 'td[class="bold text-right"]')
        #Добавляем в список данные
        data.append([name.text, final_price.text])
        #Задержка для имитации человеческой прокрутки
        time.sleep(0.2)

    for _ in range(40):
        #Прокрутка до момента, когда будут видны все записи таблицы
        action_to_tr = ActionChains(browser).scroll_by_amount(delta_x=0, delta_y=5)
        action_to_tr.perform()

    #Запись в csv файл
    writer_in_csv(data)


def view_all_page(browser, href):
    #Функция для просмотра страницы с таблицей Nifty Bank

    time.sleep(2)
    
    #GET - запрос к целевой странице
    browser.get(href)

    #Ожидаем появления select на странице
    select_element = timeout_validate(browser, el_id='equitieStockSelect')
    
    time.sleep(1)

    #Ожидаем появления option NIFTY ALPHA 50 в select
    option = timeout_option(browser, 'NIFTY ALPHA 50')

    #Перемещаемся к элементу select и кликаем по нему
    action_click = ActionChains(browser).move_to_element(select_element).click()
    action_click.perform()

    time.sleep(1)

    #Кликаем по NIFTY ALPHA 50
    option.click()

    time.sleep(1)

    #Кликаем ещё раз, чтобы закрыть Dropdown
    select_element.click()

    time.sleep(1)

    #Находим элемент Note
    scroll_element = browser.find_element(By.ID, 'market-note3')
    #Находим размер элемента
    scroll_to = scroll_element.size['width']
    
    for step in range(1, scroll_to , 2):
        #Scroll вниз таблицы
        browser.execute_script(f"window.scrollTo(0, {step});")

    time.sleep(2)


def user_script(browser):
    time.sleep(1)

    #Ожидаем появления кнопки Nifty Bank и кликаем по ней
    nifty_bank = timeout_validate(browser, el_id='tabList_NIFTYBANK').click()
    
    time.sleep(1)

    #Ищем кнопку View All
    view_all = browser.find_element(By.XPATH, '//a[contains(@href, "NIFTY BANK")]')
    #Находим координаты элемента
    scroll_to = view_all.location_once_scrolled_into_view['x']

    for step in range(1, scroll_to, 2):
        #Скроллим до элемента View All
        browser.execute_script(f"window.scrollTo(0, {step});")
    
    #Получаем ссылки из атрибута href
    href = view_all.get_attribute('href')

    #Запуск функции просмотра страницы с таблицей Nifty Bank
    view_all_page(browser, href)