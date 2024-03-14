from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from config import (set_options, timeout_validate, 
                    user_script, pre_open_page)


def main(context=None):
    with Chrome(options=set_options()) as browser:
        browser.get('https://www.nseindia.com')
        # Какой user-agent используется в данном запросе
        # print(browser.execute_script("return navigator.userAgent;"))

        market_data = timeout_validate(browser, el_id='link_2')

        action_to_graph = ActionChains(browser).move_to_element(market_data).click()
        action_to_graph.perform()

        time.sleep(1)

        pre_open_market = timeout_validate(market_data, xpath='//a[text()="Pre-Open Market"]')
        pre_open_market_href = pre_open_market.get_attribute('href')

        pre_open_page(browser, pre_open_market_href)
        
        browser.back()

        time.sleep(1)

        user_script(browser)
        
if __name__ == '__main__':
    main()