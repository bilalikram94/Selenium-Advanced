from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

class AutoComplete:
    def test(self):
        baseURL = "https://www.southwest.com/"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)
        cityField = driver.find_element_by_id("air-city-departure")
        cityField.send_keys("New York")
        print("City Name Entered")
        time.sleep(3)
        citySelect = driver.find_element(By.XPATH, "//li[@id='air-city-departure-menu-item3']")
        print("City Selected")
        citySelect.click()
        time.sleep(3)
        driver.quit()

ff = AutoComplete()
ff.test()