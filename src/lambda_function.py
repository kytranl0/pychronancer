import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1280x1696')
chrome_options.add_argument('--user-data-dir=/tmp/user-data')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--enable-logging')
chrome_options.add_argument('--log-level=0')
chrome_options.add_argument('--v=99')
chrome_options.add_argument('--single-process')
chrome_options.add_argument('--data-path=/tmp/data-path')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--homedir=/tmp')
chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"
 
driver = webdriver.Chrome(chrome_options=chrome_options)

def lambda_handler(*args, **kwargs):
    example_text = ''
    sekinAl="https://seekingalpha.com/market-news/all" 
# driver.get("http://www.python.org")
    driver.get(sekinAl)
# assert "Python" in driver.title
# driver
    elem = driver.find_elements_by_class_name("title")
    for i in elem:
        example_text = i.text
    
# /html/body/div[3]/div/div/div[2]/ul/li[2]/div[2]/div[1]
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
    driver.close()


    return example_text
