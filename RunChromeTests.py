from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class RunChromeTests():
    # https://sites.google.com/a/chromium.org/chromedriver/downloads
    # http://chromedriver.storage.googleapis.com/index.html?path=2.21/
    def test(self):
        # driverLocation = "C:\\Users\\Anil Tomar\\PycharmProjects\\libs\\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocation
        # driver = webdriver.Chrome(driverLocation)
        driver = webdriver.Chrome()
        driver.get("http://www.letskodeit.com")
        baseUrl = "https://letskodeit.teachable.com"

        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("test")

        time.sleep(3)

        emailField.clear()

        time.sleep(3)

        emailField.send_keys("test")

        driver.quit()

chromeTest = RunChromeTests()
chromeTest.test()