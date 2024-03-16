from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from fake_useragent import FakeUserAgent


def set_options() -> Options:
    #Экземпляр опций для драйвера
    options = ChromeOptions()
    #Добавление опций
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    options.add_argument("start-maximized")

    #Используем рандомный User-Agent
    options.add_argument(f'user-agent={FakeUserAgent().random}')
    #Возврат опций
    return options