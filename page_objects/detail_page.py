from selenium.webdriver.common.by import By


class DetailPage:
    def __init__(self, driver):
        self.driver = driver

    quantity = (By.ID, "quantity")
    cartButton = (By.ID, "add-to-cart-button")

    def getQuantity(self):
        return self.driver.find_element(*DetailPage.quantity)

    def addToCart(self):
        return self.driver.find_element(*DetailPage.cartButton)



