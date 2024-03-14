from selenium.webdriver import ChromeOptions
from fake_useragent import FakeUserAgent

def set_options():
    options = ChromeOptions()
    
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    options.add_argument("start-maximized")

    options.add_argument(f'user-agent={FakeUserAgent().random}')

    return options