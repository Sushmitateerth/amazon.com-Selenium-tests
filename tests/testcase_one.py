import time
from selenium.webdriver.support.select import Select

from page_objects import home_page, product_page, detail_page, cart_page
from utilities.base_class import baseClass


class TestOne(baseClass):

    def test_e2e(self):

        homepage = home_page.HomePage(self.driver)
        homepage.searchBar().send_keys("chai")
        time.sleep(1)

        productpage = product_page.ProductPage(self.driver)
        elements = productpage.getProducts()
        for el in elements:
            if el.text == "chain":
                el.click()
                break

        productpage.getProductDetails().click()
        chains = productpage.getSelectedProduct()
        for chain in chains:
            if chain.text == "Trendy Fashion Multilayered Key Heart Locket Silver Plated Chain Choker Necklace for Women and Girls":
                chain.click()

        self.childWindowShift()
        detailspage = detail_page.DetailPage(self.driver)
        self.selectFromDropDown(detailspage.getQuantity())
        detailspage.addToCart().click()
        
        cartpage = cart_page.CartPage(self.driver)
        total = cartpage.getPriceText().text
        update = total.replace("₹","").strip()
        assert update in "398.00"





