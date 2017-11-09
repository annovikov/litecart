import pytest
from selenium import webdriver
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
    driver.get("http://localhost/litecart/")
    driver.find_element_by_css_selector(".content>form>table>tbody>tr>td>a").click()
    #driver.find_element_by_name("company").click()
    driver.find_element_by_name("company").clear()
    driver.find_element_by_name("company").send_keys('market')
    driver.find_element_by_name("tax_id").clear()
    driver.find_element_by_name("tax_id").send_keys('user1')
    driver.find_element_by_name("firstname").clear()
    driver.find_element_by_name("firstname").send_keys('Lenin')
    driver.find_element_by_name("lastname").clear()
    driver.find_element_by_name("lastname").send_keys('Ilyich')
    driver.find_element_by_name("address1").clear()
    driver.find_element_by_name("address1").send_keys('Lubyanka')
    driver.find_element_by_name("address2").clear()
    driver.find_element_by_name("address2").send_keys('secret')
    driver.find_element_by_name("postcode").clear()
    driver.find_element_by_name("postcode").send_keys('64056')
    driver.find_element_by_name("city").clear()
    driver.find_element_by_name("city").send_keys('Moscow')
    #select Unated States
    driver.find_element_by_class_name("selection").click()
    driver.find_element_by_xpath("html/body/span/span/span[2]/ul/li[.='United States']").click()
    #generate random email
    data = ''.join(random.choice(string.ascii_letters) for i in range(5))+"@"+''.join(random.choice(string.ascii_letters) for i in range(5))+".com"
    print(data)
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(data)
    driver.find_element_by_name("phone").clear()
    driver.find_element_by_name("phone").send_keys('8888888')
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys('pass')
    driver.find_element_by_name("confirmed_password").clear()
    driver.find_element_by_name("confirmed_password").send_keys('pass')
    driver.find_element_by_name("create_account").click()
    #logout from created user
    driver.find_element_by_xpath(".//a[contains(text(),'Logout')]").click()
    #login
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(data)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys('pass')
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath(".//a[contains(text(),'Logout')]").click()




