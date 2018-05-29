from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SwitchtoIframe:
    def test (self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)
        driver.execute_script("window.scrollBy(0,2000);")

        # Switch to iframe using ID
        #driver.switch_to.frame("courses-iframe")
        #time.sleep(3)

        # Switch to iFrame using Name
        #driver.switch_to.frame("iframe-name")
        #time.sleep(3)

        # Switch to iFrame using Number
        driver.switch_to.frame(0)
        time.sleep(3)


        # Search Courses
        driver.find_element(By.ID, "search-courses").send_keys("Python"+Keys.ENTER)
        time.sleep(3)
        # Switch back to parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0 , -2000);")
        time.sleep(3)
        driver.find_element(By.ID,"name").send_keys("Test Successful")
        time.sleep(2)

ff = SwitchtoIframe()
ff.test()