from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


def find_hashtag(username, password, hashtag):
    browser = webdriver.Chrome('chromedriver/chromedriver')

    try:
        browser.get('https://www.instagram.com/')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element('name', 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(3)

        password_input = browser.find_element('name', 'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(15)

            for i in range(0, 10):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)

            hrefs = browser.find_elements(By.TAG_NAME, 'a')

            posts = []

            for item in hrefs:
                href = item.get_attribute('href')
                if '/p/' in href:
                    posts.append(href)

            for post in posts:
                try:
                    browser.get(post)
                    time.sleep(10)

                    like_button = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')

                    like_button.click()

                    time.sleep(5)

                    # this time.sleep for new users because new users have like limit
                    # time.sleep(random.randrange(80, 100))
                except Exception as exc:
                    print(exc)

        except Exception as ex:
            print(ex)

        browser.close()
        browser.quit()
    except Exception as e:
        print(e)
        browser.close()
        browser.quit()
