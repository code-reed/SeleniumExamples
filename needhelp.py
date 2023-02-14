from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# variables for webdriver use
ser = Service(r"/Users/erin/Documents/SeleniumDrivers/chromedriver")  # this will need to be changed ...
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


def hudl_help():
    # navigate to hudl website
    driver.get("https://www.hudl.com")

    # locate login button and click
    login = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/a[2]")
    login.click()

    # wait for the page to load
    driver.implicitly_wait(10)

    # locate need help hyperlink and click
    get_help = driver.find_element(By.LINK_TEXT, "Need help?")
    get_help.click()

    driver.implicitly_wait(10)

    # if this element is found and on display, we successfully navigated to need help page
    if driver.find_element(By.LINK_TEXT, "support@hudl.com").is_displayed():
        print("How can we help?")

    # sleep so driver doesn't immediately close
    time.sleep(10)

    # close the driver
    driver.quit()

#run method

hudl_help()
