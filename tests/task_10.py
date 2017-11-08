import pytest
from selenium import webdriver
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

def test_style(driver):
    driver.get("http://localhost/litecart/")
    name = driver.find_element_by_xpath(".//*[@id='box-campaigns']/div/ul/li/a[1]/div[2]").text
    print(name)
    old_price = driver.find_element_by_xpath(".//*[@id='box-campaigns']/div/ul/li/a[1]/div[4]/s")
    new_price = driver.find_element_by_xpath(".//*[@id='box-campaigns']/div/ul/li/a[1]/div[4]/strong")
    old_value = old_price.text
    new_value = new_price.text
    color_old = old_price.value_of_css_property("color")
    color_new = new_price.value_of_css_property("color")
    textdec = old_price.value_of_css_property("text-decoration-line")
    textboldnew = new_price.value_of_css_property("font-weight")
    textboldold = old_price.value_of_css_property("font-weight")
    size_old = old_price.size
    size_new = new_price.size
    print(old_value)
    print(new_value)
    print(color_old)
    print(color_new)
    print(textdec)
    print(textboldnew)
    print(textboldold)
    print(size_old)
    print(size_new)
    assert textboldold < textboldnew
    assert textdec == 'line-through'
    assert size_old.get("height") < size_new.get("height")
    assert size_old.get("width") < size_new.get("width")
    #open product and read properties
    driver.find_element_by_xpath(".//*[@id='box-campaigns']/div/ul/li/a[1]").click()
    name1 = driver.find_element_by_xpath(".//*[@id='box-product']/div[1]/h1").text
    print(name1)
    old_price = driver.find_element_by_xpath(".//*[@id='box-product']/div[2]/div[2]/div[2]/s")
    new_price = driver.find_element_by_xpath(".//*[@id='box-product']/div[2]/div[2]/div[2]/strong")
    old_value1 = old_price.text
    new_value1 = new_price.text
    color_old1 = old_price.value_of_css_property("color")
    color_new1 = new_price.value_of_css_property("color")
    size_old1 = old_price.size
    size_new1 = new_price.size
    print(old_value1)
    print(new_value1)
    print(color_old1)
    print(color_new1)
    print(size_old1)
    print(size_new1)

    assert size_old1.get("height") < size_new1.get("height")
    assert size_old1.get("width") < size_new1.get("width")
    #compare values between pages
    assert name == name1
    assert old_value == old_value1
    assert new_value == new_value1
