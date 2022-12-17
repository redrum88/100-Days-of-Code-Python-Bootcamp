from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


# Settings
FOLLOW_COUNT = 10
ACCOUNT_CHECK = "waiifumia"          # Enter account name from which you will retrieve followers
ACCOUNT_FOLLOWER = "following"       # Enter 'following' or 'followers' to choose what you want to follow.
USERNAME = "your username"           # Enter your instagram username
PASSWORD = "your password"           # Enter password
URL = "https://www.instagram.com/"

class InstaFollower:

    def __init__(self):
        self.SERVICE = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.SERVICE)
        self.driver.get(URL)
        self.driver.maximize_window()
        sleep(10)

    def login(self):
        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.RETURN)
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '._ac8f button').click()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '._a9-z button').click()
        sleep(3)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{ACCOUNT_CHECK}/{ACCOUNT_FOLLOWER}")
        sleep(3)

    def follow(self):
        count_down = FOLLOW_COUNT
        power = True
        while power:
            try:
                all_users = self.driver.find_elements(By.CSS_SELECTOR, 'button')
                for user in all_users:
                    if user.text == "Follow" and count_down > 1:
                        user.click()
                        count_down -= 1
                        sleep(random.randint(3, 60))
                    print(len(all_users))
                    print(f"Count down: {count_down}")

                self.driver.execute_script("argument[0].scrollIntoView(true);", all_users[-1])

            except Exception as e:
                print(e)
            if count_down < 1:
                power = False


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()