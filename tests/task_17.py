import pytest
from selenium import webdriver
import os
import string
import random
from random import choice
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    # wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox_56\\firefox.exe")
    wd = webdriver.Firefox(capabilities={"marionette": False},
                           firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
    # wd = webdriver.Chrome()
    # wd = webdriver.Ie()
    # print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_logs(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath(".//*[@id='box-apps-menu']//span[.='Catalog']").click()
    # раскрытие папок
    folder_count = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr/td[3]/i/../a")
    while len(folder_count) > 0:
        driver.find_element_by_xpath(".//*[@id='content']/form/table/tbody/tr/td[3]/i/../a").click()
        folder_count = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr/td[3]/i/../a")
    # кликанье по товарам
    element_count = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr/td[3]/a")
    for element in range(0, len(element_count)):
        element_count = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr/td[3]/a")
        element_count[element].click()
        for l in driver.get_log("browser"):
            print(l)
        driver.find_element_by_xpath(".//*[@id='content']/form/p/span/button[2]").click()

