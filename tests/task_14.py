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
    #wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox_56\\firefox.exe")
    wd = webdriver.Firefox(capabilities={"marionette": False}, firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
    #wd = webdriver.Chrome()
    #wd = webdriver.Ie()
    #print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_windows(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath(".//*[@id='box-apps-menu']//span[.='Countries']").click()
    driver.find_element_by_xpath(".//*[@id='content']/div/a").click()
    ext_links = driver.find_elements_by_css_selector(".fa.fa-external-link")
    for countL in range (0, len(ext_links)):
        main_window = driver.current_window_handle
        old_windows = driver.window_handles
        ext_links[countL].click()
        wait.until(expected_conditions.new_window_is_opened(old_windows))
        new_windows = driver.window_handles
        new_window = list(set(new_windows).difference(old_windows))
        #assert old_windows == new_windows
        driver.switch_to_window(new_window)
        driver.close()
        driver.switch_to_window(main_window)
    driver.find_element_by_css_selector(".fa.fa-sign-out.fa-lg").click()





