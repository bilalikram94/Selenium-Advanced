from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ScrollingElement:
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)
        #Scroll Down
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        # Scroll Up
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(2)
        # Scroll Element Into View
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-150);")
        time.sleep(2)
        #Native Way to Scroll Element into View
        driver.execute_script("window.scrollBy(0,-1000);")
        location = element.location_once_scrolled_into_view
        time.sleep(2)
        print(" Location: " + str(location))


ff = ScrollingElement()
ff.test()