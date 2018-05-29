from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SwitchToWindow:
    def test (self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)
        # Find parent Handle --> Main Window

        parentHandle = driver.current_window_handle
        print("Parent Handle:" + parentHandle)

        # Find open Window Button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all Handles, There should be two handles after clicking open window button\
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:

            print("Handle:" + handle)

            if handle not in parentHandle:

                driver.switch_to.window(handle)

                print("switched to window : :" +handle)

                searchbox = driver.find_element(By.ID, "search-courses")

                searchbox.send_keys("python" + Keys.ENTER)

                time.sleep(3)

                driver.close()
                break
        # Switch to parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID,"name").send_keys("Test successfully")
        time.sleep(3)
        driver.quit()


ff = SwitchToWindow()
ff.test()