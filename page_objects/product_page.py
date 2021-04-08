from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    allProducts = (By.CLASS_NAME, "s-suggestion")
    productDetail = (By.ID, "p_89/Yellow Chimes")
    selectedProduct = (By.CSS_SELECTOR, "[class = 'a-link-normal a-text-normal']")

    def getProducts(self):
        return self.driver.find_elements(*ProductPage.allProducts)

    def getProductDetails(self):
        return self.driver.find_element(*ProductPage.productDetail)

    def getSelectedProduct(self):
        return self.driver.find_elements(*ProductPage.selectedProduct)