from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import time

SERVICE = Service(ChromeDriverManager().install())
URL = "http://orteil.dashnet.org/experiments/cookie/"
minutes = int(input("Enter time in minutes: "))
if minutes:
    # Open site
    driver = webdriver.Chrome(service=SERVICE)
    driver.get(URL)

    cookie = driver.find_element(By.ID, "cookie")
    items = driver.find_elements(By.CSS_SELECTOR,"#store div")

    item_ids = [item.get_attribute("id") for item in items]



    timeout = time() + 5
    time_to_run = time() + 60 * minutes

    while True:
        cookie.click()

        # Every 5 seconds:
        if time() > timeout:

            # Get all upgrade <b> tags
            all_prices = driver.find_elements(By.CSS_SELECTOR,"#store b")
            item_prices = []

            # Convert <b> text into an integer price.
            for price in all_prices:
                element_text = price.text
                if element_text != "":
                    cost = int(element_text.split("-")[1].strip().replace(",", ""))
                    item_prices.append(cost)

            # Create dictionary of store items and prices
            cookie_upgrades = {}
            for n in range(len(item_prices)):
                cookie_upgrades[item_prices[n]] = item_ids[n]

            # Get current cookie count
            money_element = driver.find_element(By.ID,"money").text
            if "," in money_element:
                money_element = money_element.replace(",", "")
            cookie_count = int(money_element)

            # Find upgrades that we can currently afford
            affordable_upgrades = {}
            for cost, id in cookie_upgrades.items():
                if cookie_count > cost:
                    affordable_upgrades[cost] = id

            # Purchase the most expensive affordable upgrade
            highest_price_affordable_upgrade = max(affordable_upgrades)
            print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element(By.ID, to_purchase_id).click()

            # Add another 5 seconds until the next check
            timeout = time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
        if time() > time_to_run:
            cookie_per_s = driver.find_element(By.ID, "cps").text
            print(cookie_per_s)
            break