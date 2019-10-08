"""
This module contains step definitions for table_filter.feature.
"""

import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.keys import Keys
from dental.pages.task_filter.task_page import TaskFilter

# Constants

TASK_TABLE_URL = 'https://www.seleniumeasy.com/test/table-search-filter-demo.html'

# Scenarios
CONVERTERS = dict(criteria=str, occurrence=int)
scenarios('../features/table_filter.feature', example_converters=CONVERTERS)


# Given Steps
@given("the task table is displayed")
def go_to_task_page(driver):
    driver.get(TASK_TABLE_URL)


# When Steps
@when('i enter the task name as search <criteria>')
@when('i enter the assignee name as search <criteria>')
@when('i enter the task status as search <criteria>')
@when('i enter an unavailable search <criteria>')
@when(parsers.parse('i enter an unavailable search {criteria}'))
def enter_task_name_as_search_criteria(driver, criteria):
    page = TaskFilter(driver)
    page.enter_search_criteria(search_criteria=criteria + Keys.RETURN)


# Then Steps
@then('the table should contains only the task matching the search <criteria> name')
@then(parsers.parse('the table should contains only the task matching the search {criteria} name'))
def check_table_row_contains_selected_task(driver, criteria):
    search_result = None
    page = TaskFilter(driver)
    search_result = page.find_search_result_row(search_criteria=criteria)
    assert search_result is not None and len(search_result) == 1


@then('the table should contains the tasks matching the <criteria> with the correct <occurrence>')
@then(parsers.parse('the table should contains the tasks matching the {criteria} with the correct {occurrence:d}'))
def check_tasks_matching_criteria(driver, criteria, occurrence):
    search_results = None
    page = TaskFilter(driver)
    search_results = page.find_search_result_row(search_criteria=criteria)
    assert search_results is not None and len(search_results) == occurrence


@then(parsers.parse('the table should contains the message "{message}"'))
def check_not_found_message_displayed(driver, message):
    page = TaskFilter(driver)
    assert page.check_no_result_message().text == message
