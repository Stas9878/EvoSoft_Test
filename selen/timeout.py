from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def timeout_validate(browser, el_id=None, xpath=None):
    #Функция для ожидания появления целевого элемента на странице
    try:
        settings = {
            'el_id': By.ID,
            'xpath': By.XPATH,
        }

        if el_id:
            #Если передали id, то класс селектора By.ID
            class_by, arg = settings['el_id'], el_id
        elif xpath:
            #Если передали id, то класс селектора By.XPATH
            class_by, arg = settings['xpath'], xpath
        #Ожидаем появления целевого элемента на странице
        result = WebDriverWait(browser, timeout=10).until(
                    EC.presence_of_element_located((class_by, arg))
            )
        #Возвращаем его
        return result
    
    except TimeoutException:
        #Если не дождались элемент райзим ошибку
        raise TimeoutException('Произошла ошибка поиска элемента, попробуйте увеличить timeout')
    

def timeout_option(browser, value):
    result = WebDriverWait(browser, timeout=10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, f'option[value="{value}"]'))
    )
    return result
