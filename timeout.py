from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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