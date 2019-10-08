from selenium.webdriver.common.by import By
from dental.base.selenium_driver import SeleniumDriver


class TaskFilter(SeleniumDriver):
    """
    Implementing the Page object Model design pattern
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_filter_field = 'task-table-filter'
    _no_result_selector = "//*[@id='task-table']/tbody/tr[contains(@class,'filterTable_no_results')]"

    def enter_search_criteria(self, search_criteria):
        """
        enter the search criteria on the search bar
        :param search_criteria:
        :return:
        """
        self.send_element_keys(search_criteria, self._search_filter_field)

    def find_search_result_row(self, search_criteria):
        """
        return all the elements matching the search criteria
        :param search_criteria:
        :return:
        """
        return self.get_elements(
            f"//*[@id='task-table']/tbody/tr[not(contains(@style,'display: none'))]/td[contains(text(),'{search_criteria}')]",
            "xpath")

    def check_no_result_message(self):
        """
        return the row containing the No Result message
        :return:
        """
        return self.get_element(self._no_result_selector,"xpath")