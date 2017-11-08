import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    #wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox_56\\firefox.exe")
    wd = webdriver.Firefox(capabilities={"marionette": False}, firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
    #wd = webdriver.Chrome()
    #wd = webdriver.Ie()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_country(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    list_country = []
    country_count = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr")
    for country in range(1, len(country_count)-1):
        country_count = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr")
        text = country_count[country].find_element_by_xpath("td[5]").text
        zones = country_count[country].find_element_by_xpath("td[6]").text
        list_country.append(text)
        if int(zones) > 0:
            print(zones)
            list_zones = []
            country_count[country].find_element_by_xpath("td[5]/a").click()
            zone_count = driver.find_elements_by_xpath(".//*[@id='table-zones']/tbody/tr/td[3]")
            for item in range(0, len(zone_count)-1):
                zone_name = zone_count[item].text
                list_zones.append(zone_name)
            assert list_zones ==sorted(list_zones)
            driver.find_element_by_xpath(".//*[@id='content']/form/p/span/button[2]").click()

    print(list_country)
    assert list_country == sorted(list_country)


def test_geo_zones(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    country_list = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr/td[3]")
    for country in range(0, len(country_list)):
        country_list = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr/td[3]")
        country_list[country].find_element_by_xpath("a").click()
        WebDriverWait(driver, 15).until(EC.title_is("Edit Geo Zone | My Store"))
        list_zones_visible = []
        for zones in driver.find_elements_by_xpath(
            ".//*[@id='table-zones']/tbody/tr/td/select[starts-with(@name,'zones[') and not(contains (@aria-hidden,'true'))]/option[@selected='selected']"):
            zone_name = zones.text
            list_zones_visible.append(zone_name)
        assert list_zones_visible == sorted(list_zones_visible)
        driver.find_element_by_xpath(".//*[@id='content']/form/p/span/button[2]").click()




