import time

from webdriver_wrapper import WebDriverWrapper
from selenium.webdriver.common.keys import Keys


def lambda_handler(*args, **kwargs):
    driver = WebDriverWrapper()
    example_text = ''
    sekinAl="https://seekingalpha.com/market-news/all" 
# driver.get("http://www.python.org")
    driver.get(sekinAl)
# assert "Python" in driver.title
# driver
    elem = driver.find_elements_by_class_name("title")
    for i in elem:
        if 'doge' in i.text
        print(i.text)
    
# /html/body/div[3]/div/div/div[2]/ul/li[2]/div[2]/div[1]
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
    driver.close()


    return example_text
