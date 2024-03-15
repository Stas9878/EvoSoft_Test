from selenium.webdriver import ChromeOptions
from fake_useragent import FakeUserAgent
from writer_csv import writer_in_csv
from timeout import timeout_validate
from user_script import user_script, pre_open_page


def set_options():
    options = ChromeOptions()
    
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    options.add_argument("start-maximized")

    options.add_argument(f'user-agent={FakeUserAgent().random}')

    return options