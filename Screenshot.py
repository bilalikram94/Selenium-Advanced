from selenium import  webdriver
from  selenium.webdriver.common.by import By
import time

baseURL = "https://learn.letskodeit.com/"
driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")

class Screenshots:
    def test(self):
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc123")
        driver.find_element(By.NAME, "commit").click()
        destinationFileName = "C:\\Users\\Bilal.Ikram\\Desktop\\test.png"

        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot saved to directory --> :: " + destinationFileName)

        except NotADirectoryError:
            print("not a directory")

ff = Screenshots()
ff.test()