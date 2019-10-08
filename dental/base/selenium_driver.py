
from selenium.webdriver.common.by import By
from traceback import print_stack


class SeleniumDriver:
    """
    Provide the basis functionality for a framework around selenium
    webdriver
    """
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_by_type(locator_type):
        """

        :param locator_type:
        :return:
        """
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            print(f"Locator type :{locator_type} not correct/supported")
        return False

    def get_element(self, locator, locator_type):

        """
         return the element matching the @locator
        :param locator:
        :param locator_type:
        :return:
        """
        element = None
        try:
            type = locator_type.lower()
            by_type = self.get_by_type(type)
            element = self.driver.find_element(by_type, locator)
            print("Element Found with locator: " + locator + " and  locatorType: " + locator_type)
        except:
            print("Element not found")
        return element

    def get_elements(self, locator, locator_type):

        """
         return an array containing the elements matching the @locator
        :param locator:
        :param locator_type:
        :return:
        """
        elements = None
        try:
            type = locator_type.lower()
            by_type = self.get_by_type(type)
            elements = self.driver.find_elements(by_type, locator)
            print("Element Found with locator: " + locator + " and  locatorType: " + locator_type)
        except:
            print("Element not found")
        return elements

    def element_click(self, locator, locator_type="id"):

        """
         click on the element located by the @locator
        :param locator:
        :param locator_type:
        :return:
        """
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            print(f"Clicked on the element located by {locator} - locator type {locator_type}")
            return True
        except:
            print(f"Can't clicked on the element located by {locator} - locator type {locator_type}")
            print_stack()
            return False

    def send_element_keys(self, data, locator, locator_type="id"):
        """
        Enter data to the field located by @locator
        :param data:
        :param locator:
        :param locator_type:
        :return:
        """
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            print("Sent data on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            print("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locator_type)
            print_stack()
