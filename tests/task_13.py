import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
import time
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

def test_add_user(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/")
    for i in range(1, 4):
        driver.find_element_by_xpath(".//*[@id='box-most-popular']/div/ul/li[1]/a[1]").click()
        # if we try to add yellow duck
        if len(driver.find_elements_by_name("options[Size]")) > 0:    # driver.find_element_by_name("options[Size]").is_displayed
            driver.find_element_by_xpath(".//*[@id='box-product']/div[2]/div[2]/div[5]/form/table/tbody/tr[1]/td/select/option[2]").click()
        driver.find_element_by_name("add_cart_product").click()
        wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//*[@id='cart']/a[2]/span[1]"), str(i)))
        print(driver.find_element_by_xpath(".//*[@id='cart']/a[2]/span[1]").text)
        driver.find_element_by_xpath(".//*[@id='breadcrumbs']/ul/li[1]/a").click()
    driver.find_element_by_xpath(".//*[@id='cart']/a[3]").click()
    #count = driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody//td[3]")
    #print(len(count))
    #deleting
    while len(driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody//td[3]")) > 0:
        wait.until(expected_conditions.element_to_be_clickable((By.NAME, "remove_cart_item"))).click()
        time.sleep(2)
        count_new = len(driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody//td[3]"))
        print("Remains "+str(count_new)+" items")
    time.sleep(5)
    assert len(driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody//td[3]"))==0








