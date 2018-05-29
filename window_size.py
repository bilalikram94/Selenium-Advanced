from selenium import webdriver
from selenium.webdriver.common.by import By
import  time

class WindowSize:
    def test(self):
        baseURL = "https://learn.letskodeit.com/"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        #driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        height = driver.execute_script("return window.innerHeight;")

        width = driver.execute_script("return window.innerWidth;")

        print("Height:" + str(height))

        print("Width" + str(width))
        driver.quit()

ff = WindowSize()
ff.test()
