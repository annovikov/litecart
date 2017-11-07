import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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

def test_menu_admin(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    main_menu = driver.find_elements_by_xpath(".//*[@id='app-']")
    for countM in range(0, len(main_menu)):
        main_menu = driver.find_elements_by_xpath(".//*[@id='app-']")
        main_menu[countM].click()
        driver.find_element_by_xpath(".//*[@id='content']/h1")
        under_menu = driver.find_elements_by_xpath(".//*[@id='app-']/ul/li")
        for countU in range(0, len(under_menu)):
            under_menu = driver.find_elements_by_xpath(".//*[@id='app-']/ul/li")
            under_menu[countU].click()
            driver.find_element_by_xpath(".//*[@id='content']/h1")


    driver.find_element_by_css_selector(".fa.fa-sign-out.fa-lg").click()





