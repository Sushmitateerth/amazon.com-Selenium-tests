from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    priceText = (By.CSS_SELECTOR, "[class = 'a-color-price hlb-price a-inline-block a-text-bold']")

    def getPriceText(self):
        return self.driver.find_element(*CartPage.priceText)