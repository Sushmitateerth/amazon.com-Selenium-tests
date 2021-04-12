from selenium.webdriver.common.by import By


class HomeDecorPage:
    def __init__(self, driver):
        self.driver = driver

    maxvalue = (By.XPATH, "//span[contains(text(), 'Under ₹500')]")
    filteramount = (By.ID, "high-price")
    go = (By.XPATH, "//form/span/span[@class='a-button-inner']")
    allelements = (By.CSS_SELECTOR, "[class='a-size-base-plus a-color-base a-text-normal']")


    def getMaxValue(self):
        return self.driver.find_element(*HomeDecorPage.maxvalue)

    def getFilterAmount(self):
        return self.driver.find_element(*HomeDecorPage.filteramount)

    def getGoButton(self):
        return self.driver.find_element(*HomeDecorPage.go)

    def getAllElements(self):
        return self.driver.find_elements(*HomeDecorPage.allelements)