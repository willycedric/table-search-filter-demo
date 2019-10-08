"""
This module contains shared fixtures, steps, and hooks.
"""
from selenium import webdriver
import pytest

# Fixtures

@pytest.fixture
def driver():
    b = webdriver.Firefox()
    b.maximize_window()
    b.implicitly_wait(10)
    yield b
    b.quit()


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')




#https://stackoverflow.com/questions/51303649/python-selenium-using-same-driver-instance-which-is-initiated-in-another-file
#Screenplay Pattern - an other page desing pattern which is presented as an alternative to the page object model


