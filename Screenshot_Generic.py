from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class Screenshots:
    def test(self):
        baseURL = "https://learn.letskodeit.com/"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc123")
        driver.find_element(By.NAME, "commit").click()
        self.takeScreenshot(driver)



    def takeScreenshot(self,driver):
        """
         Takes Screenshots of the current open tab
        :param driver:
        :return:

        """
        filename = str(round(time.time()*1000)) + ".png"
        screenshotdirectory = "C:\\Users\\Bilal.Ikram\\Desktop\\"
        destinationfile = screenshotdirectory + filename

        try:
            driver.save_screenshot(destinationfile)
            print("Screenshot saved to directory --> :: " + destinationfile)

        except NotADirectoryError:
            print("not a directory")


ff = Screenshots()
ff.test()