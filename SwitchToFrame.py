from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToFrame:
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        driver.find_element(By.ID, "name").send_keys("Bilal")
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(3)

        driver.find_element(By.ID, "name").send_keys("Bilal")
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)
        alert2 = driver.switch_to.alert
        alert2.dismiss()


ff = SwitchToFrame()
ff.test()