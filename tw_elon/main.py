from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

def rss_app(browser, url):
    browser.get('https://rss.app/rss-feed/create-twitter-rss-feed')

    inpt = browser.find_element(By.ID, ':r0:')
    inpt.send_keys(url)
    button_accept = browser.find_element(By.ID, 'provider-submit').click()
    
    feed = WebDriverWait(browser, timeout=20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'tss-k2zsea-FeedCardOverview-content'))
    )

    return browser

    
def main(browser, feed):
    browser.get('https://rss.app/feed/ibaOnSgxKUkOOusk')
        
    posts = []

    while len(posts) < 10:
        ac_scroll = ActionChains(browser).scroll_by_amount(delta_x=0, delta_y=2000)
        ac_scroll.perform()
        posts = posts = browser.find_elements(By.XPATH, '//a[@class="MuiTypography-root MuiTypography-h3 tss-1h8hsy-FeedCardOverview-title mui-1ti1707-Typography-fontWeightBold"]')
    
    for num, post in enumerate(posts[:10], 1):
        text = post.text        
        print(f'Пост #{num}:\n\t{text if text else "Текст отсутствует"}\n')
    
if __name__ == '__main__':
    with Chrome() as browser:
        user_url = 'https://twitter.com/elonmusk'

        feed = rss_app(browser, user_url)

        main(feed)