from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class DragDrop:
    def test(self):
        baseURL = "http://jqueryui.com/droppable/"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)
        driver.switch_to.frame(0)
        fromElement = driver.find_element(By.ID,"draggable")
        toElement = driver.find_element(By.ID,"droppable")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            #actions.drag_and_drop(fromElement, toElement).perform()
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("element dragged and dropped successfully")
            time.sleep(3)



        except:
            print("No Such Element")

ff = DragDrop()
ff.test()