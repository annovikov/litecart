import pytest
from selenium import webdriver
import os
import string
import random
from random import choice
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
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

def test_add_product(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath(".//*[@id='box-apps-menu']//span[.='Catalog']").click()
    driver.find_element_by_xpath(".//*[@id='content']/div[1]/a[2]").click()
    #fill forms
    if not driver.find_element_by_xpath(".//*[@id='tab-general']/table/tbody/tr[1]/td/label[1]/input").is_selected():
        driver.find_element_by_xpath(".//*[@id='tab-general']/table/tbody/tr[1]/td/label[1]/input").click()
    driver.find_element_by_name("name[en]").clear()
    driver.find_element_by_name("name[en]").send_keys('Mega product')
    driver.find_element_by_name("code").clear()
    driver.find_element_by_name("code").send_keys('Mega DUCK')
    if not driver.find_element_by_xpath(".//*[@id='tab-general']/table/tbody/tr[7]/td/div/table/tbody/tr[4]/td[1]/input").is_selected():
        driver.find_element_by_xpath(".//*[@id='tab-general']/table/tbody/tr[7]/td/div/table/tbody/tr[4]/td[1]/input").click()
    driver.find_element_by_name("new_images[]").send_keys(os.path.abspath("logo.jpg"))

    #page Information
    driver.find_element_by_xpath(".//*[@id='content']/form/div/ul//a[.='Information']").click()
    driver.find_element_by_xpath(".//*[@id='tab-information']/table/tbody/tr[1]/td/select/option[.='ACME Corp.']").click()
    driver.find_element_by_name("keywords").clear()
    driver.find_element_by_name("keywords").send_keys('Mega')
    driver.find_element_by_name("short_description[en]").clear()
    driver.find_element_by_name("short_description[en]").send_keys('the best product')
    driver.find_element_by_name("head_title[en]").clear()
    driver.find_element_by_name("head_title[en]").send_keys('you must by it')
    # page Price
    driver.find_element_by_xpath(".//*[@id='content']/form/div/ul/li[4]/a").click()
    driver.find_element_by_name("purchase_price").clear()
    driver.find_element_by_name("purchase_price").send_keys('150')
    driver.find_element_by_xpath(".//*[@id='tab-prices']/table[1]/tbody/tr/td/select/option[.='US Dollars']").click()
    driver.find_element_by_name("prices[USD]").clear()
    driver.find_element_by_name("prices[USD]").send_keys('150')
    driver.find_element_by_name("save").click()
    # check added product
    assert driver.find_element_by_xpath(".//*[@id='content']/form/table/tbody//td/a[.='Mega product']")
    driver.find_element_by_css_selector(".fa.fa-sign-out.fa-lg").click()

