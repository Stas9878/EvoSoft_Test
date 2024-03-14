from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from config import set_options

def timeout_validate(browser, el_id=None, xpath=None):
    try:
        settings = {
            'el_id': By.ID,
            'xpath': By.XPATH,
        }

        if el_id:
            class_by, arg = settings['el_id'], el_id
        elif xpath:
            class_by, arg = settings['xpath'], xpath

        result = WebDriverWait(browser, timeout=10).until(
                    EC.presence_of_element_located((class_by, arg))
            )
        
        return result
    
    except:
        raise Exception('Произошла ошибка поиска элемента, попробуйте увеличить timeout')

def pre_open_page(browser, href):
    browser.get(href)

    timeout_validate(browser, el_id='livePreTable')

    tbody = browser.find_element(By.TAG_NAME, 'tbody')
    tr_table = tbody.find_elements(By.TAG_NAME, 'tr')[:-1]

    for tr in tr_table:
        action_to_tr = ActionChains(browser).move_to_element(tr)
        action_to_tr.perform()
        
        name = tr.find_element(By.CLASS_NAME, 'symbol-word-break')
        final_price = tr.find_element(By.CSS_SELECTOR, 'td[class="bold text-right"]')



def main(context=None):
    with Chrome(options=set_options()) as browser:
        browser.get('https://www.nseindia.com')
        
        #Какой user-agent используется в данном запросе
        # print(browser.execute_script("return navigator.userAgent;"))

        market_data = timeout_validate(browser, el_id='link_2')

        action_to_graph = ActionChains(browser).move_to_element(market_data).click()
        action_to_graph.perform()

        time.sleep(1)
        pre_open_market = timeout_validate(market_data, xpath='//a[text()="Pre-Open Market"]')
        pre_open_market_href = pre_open_market.get_attribute('href')

        pre_open_page(browser, pre_open_market_href)
        time.sleep(1111)
        
        


if __name__ == '__main__':
    context = {
        'proxy': [],
        'pre_open_market_href': '/market-data/pre-open-market-cm-and-emerge-market',

    }

    main()