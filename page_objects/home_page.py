from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search = (By.ID, "twotabsearchtextbox")
    decornavigation = (By.XPATH, "//span[contains(text(),'Home decoration')]")


    def searchBar(self):
        return self.driver.find_element(*HomePage.search)

    def getHomeDecor(self):
        return self.driver.find_element(*HomePage.decornavigation)

