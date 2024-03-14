from selenium.webdriver.common.by import By
from timeout import timeout_validate
import time

def pre_open_page(browser, href):
    browser.get(href)

    timeout_validate(browser, el_id='livePreTable')

    return   
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
    browser.get(href)

    timeout_validate(browser, el_id='equitieStockSelect')

    
    time.sleep(11)


def user_script(browser):
    nifty_bank = timeout_validate(browser, el_id='tabList_NIFTYBANK').click()
    
    view_all = browser.find_element(By.XPATH, '//a[contains(@href, "NIFTY BANK")]')
    scroll_to = view_all.location_once_scrolled_into_view['x']
    
    for i in range(1, scroll_to, 2):
        browser.execute_script(f"window.scrollTo(0, {i});")

    href = view_all.get_attribute('href')

    view_all_page(browser, href)