from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from timeout import timeout_validate, timeout_option
from writer_csv import writer_in_csv
import time

def pre_open_page(browser, href):
    browser.get(href)

    timeout_validate(browser, el_id='livePreTable')

    tbody = browser.find_element(By.TAG_NAME, 'tbody')
    
    tr_table = tbody.find_elements(By.TAG_NAME, 'tr')[:-1]
    
    data = []
    for tr in tr_table:
        action_to_tr = ActionChains(browser).move_to_element(tr)
        action_to_tr.perform()
        
        name = tr.find_element(By.CLASS_NAME, 'symbol-word-break')
        final_price = tr.find_element(By.CSS_SELECTOR, 'td[class="bold text-right"]')

        data.append([name.text, final_price.text])

    writer_in_csv(data)


def view_all_page(browser, href):
    time.sleep(2)
    
    browser.get(href)

    select_element = timeout_validate(browser, el_id='equitieStockSelect')
    
    time.sleep(1)

    option = timeout_option(browser, 'NIFTY ALPHA 50')

    action_click = ActionChains(browser).move_to_element(select_element).click()
    action_click.perform()

    time.sleep(1)
    option.click()
    time.sleep(1)
    select_element.click()

    time.sleep(1)

    scroll_element = browser.find_element(By.ID, 'market-note3')
    scroll_to = scroll_element.size['width']
    
    for step in range(1, scroll_to , 2):
        browser.execute_script(f"window.scrollTo(0, {step});")

    time.sleep(2)


def user_script(browser):
    time.sleep(1)

    nifty_bank = timeout_validate(browser, el_id='tabList_NIFTYBANK').click()
    time.sleep(1)

    view_all = browser.find_element(By.XPATH, '//a[contains(@href, "NIFTY BANK")]')
    scroll_to = view_all.location_once_scrolled_into_view['x']

    for step in range(1, scroll_to, 2):
        browser.execute_script(f"window.scrollTo(0, {step});")
    
    href = view_all.get_attribute('href')

    view_all_page(browser, href)