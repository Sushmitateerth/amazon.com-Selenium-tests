from page_objects import home_page, homedecor_page
from utilities.base_class import baseClass


class TestCaseTwo(baseClass):

    def test_case_two(self):

        list = []
        homepage = home_page.HomePage(self.driver)
        homepage.getHomeDecor().click()
        homedecor = homedecor_page.HomeDecorPage(self.driver)
        homedecor.getMaxValue().click()
        homedecor.getFilterAmount().clear()
        homedecor.getFilterAmount().send_keys("18")
        homedecor.getGoButton().click()
        storeElements = homedecor.getAllElements()
        for element in storeElements:
            collected = element.text
            list.append(collected)
        list.sort()
        print(list)