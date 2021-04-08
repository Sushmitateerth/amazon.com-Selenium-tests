import logging

import pytest
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")

class baseClass():
    def getLogs(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler("amazon.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)

        return logger

    def childWindowShift(self):
        childindow = self.driver.window_handles[1]
        self.driver.switch_to.window(childindow)

    def selectFromDropDown(self,element):
        select = Select(element)
        select.select_by_visible_text("2")

