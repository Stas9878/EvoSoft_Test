from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import FakeUserAgent
import time

def timeout_validate(browser, class_name=None, xpath=None):
    try:
        if class_name:
            result = WebDriverWait(browser, timeout=10).until(
                        EC.presence_of_element_located((By.ID, class_name))
                )
        elif xpath:
            result = WebDriverWait(browser, timeout=10).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                )
        return result
    
    except:
        raise Exception('Произошла ошибка поиска элемента, попробуйте увеличить timeout')

def set_options():
    options = ChromeOptions()
    
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    options.add_argument("start-maximized")

    options.add_argument(f'user-agent={FakeUserAgent().random}')

    return options

def main(context=None):
    with Chrome(options=set_options()) as browser:
        browser.get('https://www.nseindia.com')
        
        #Какой user-agent используется в данном запросе
        # print(browser.execute_script("return navigator.userAgent;"))

        market_data = timeout_validate(browser, 'link_2')

        action_to_graph = ActionChains(browser).move_to_element(market_data).click()
        action_to_graph.perform()

        time.sleep(1)
        pre_open_market = browser.find_element(By.XPATH, '//a[text()="Pre-Open Market"]')
        pre_open_market_href = pre_open_market.get_attribute('href')

        browser.get('https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market')
        time.sleep(1111)
        
        


if __name__ == '__main__':
    context = {
        'proxy': [],
        'pre_open_market_href': '/market-data/pre-open-market-cm-and-emerge-market',

    }

    main()