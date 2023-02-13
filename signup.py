from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# variables for webdriver use
ser = Service(r"/Users/erin/Documents/SeleniumDrivers/chromedriver")  # this will need to be changed ...
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


def hudl_signup():
    # navigate to hudl website
    driver.get("https://www.hudl.com")

    # locate login button and click
    login = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/a[2]")
    login.click()

    # wait for the page to load
    driver.implicitly_wait(10)

    # locate signup hyperlink and click
    create_account = driver.find_element(By.XPATH, "//*[@id='app']/section/div[2]/a")
    create_account.click()

    driver.implicitly_wait(10)

    # if this element is found and on display, we successfully navigated to signup page
    if driver.find_element(By.LINK_TEXT, "invite code").is_displayed():
        print("Sign on up!")

    # sleep so program driver immediately close
    time.sleep(10)

    # close the driver
    driver.quit()
    
# run method

hudl_signup()
