import pytest
from selenium import webdriver
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

def test_check_sticker(driver):
    driver.get("http://localhost/litecart/")
    ducks_count = driver.find_elements_by_css_selector(".image-wrapper")
    for duck in range(0, len(ducks_count)):
        item_new = ducks_count[duck].find_elements_by_css_selector(".sticker.new")
        item_sale = ducks_count[duck].find_elements_by_css_selector(".sticker.sale")
        assert len(item_sale) + len(item_new) == 1









