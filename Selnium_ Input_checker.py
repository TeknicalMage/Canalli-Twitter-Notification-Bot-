import time
import random
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
import pickle
import tweepy


consumer_key = ('')
consumer_secret = ('')
access_token = ('')
access_token_secret = ('')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)




def find():
    print(1)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    f = f = open("nt.txt", "a")
    driver.get('https://www.canlii.org/en/on/#search/type=decision&jId=on,unspecified&sort=decisionDateDesc&text=%22Employment%20Law%22&includeSccJudgments=true&origJId=on')
    x = driver.find_element_by_xpath('//a[@data-result-index="1"]').get_attribute('href')
    print(x)
    z = str(x)
    print(z)
    f.write(z)
    f.close()
    
def find_replace():
    print(1)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    f = f = open("nt.txt", "w")
    driver.get('https://www.canlii.org/en/on/#search/type=decision&jId=on,unspecified&sort=decisionDateDesc&text=%22Employment%20Law%22&includeSccJudgments=true&origJId=on')
    x = driver.find_element_by_xpath('//a[@data-result-index="1"]').get_attribute('href')
    print(x)
    z = str(x)
    print(z)
    f.write(z)
    api.update_status("New Employment Law Case " + z)
    f.close()
    prove()

def prove():
    f = f = open("nt.txt", "r")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    y = (f.readline())

    driver.get('https://www.canlii.org/en/on/#search/type=decision&jId=on,unspecified&sort=decisionDateDesc&text=%22Employment%20Law%22&includeSccJudgments=true&origJId=on')
    
    x = driver.find_element_by_xpath('//a[@data-result-index="1"]').get_attribute('href')
    z = str(x)
   
    if z == y:
        print('yes')
        print('Do nothing Conditon')
        driver.close()
    else:
        print('do something condition')
        print('no')
        find_replace()

while True:
    try:
        prove()
        time.sleep(7200)
    except:
        pass