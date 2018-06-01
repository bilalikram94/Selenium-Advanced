from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class MouseHovering:
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome(
            "C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-150);")
        time.sleep(2)
        itemToClickLocator = ".//div[@class = 'mouse-hover-content']//a[text()='Top']"
        # noinspection PyBroadException
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on Element")
            time.sleep(2)
            toplink = driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(toplink).click().perform()
            time.sleep(2)
            print("Item Clicked")
        except:
            print("Mouse Hover Failed on element")


ff = MouseHovering()
ff.test()
