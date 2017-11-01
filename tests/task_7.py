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


def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))
    # Menu Appearence
    driver.find_element_by_xpath("//span[contains(text(),'Appearence')]").click()
    driver.find_element_by_id("doc-template").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Template')]")))
    driver.find_element_by_id("doc-logotype").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Logotype')]")))
    # Menu Catalog
    driver.find_element_by_xpath("//span[contains(text(),'Catalog')]").click()
    driver.find_element_by_id("doc-catalog").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Catalog')]")))
    driver.find_element_by_id("doc-product_groups").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Product Groups')]")))
    driver.find_element_by_id("doc-option_groups").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Option Groups')]")))
    driver.find_element_by_id("doc-manufacturers").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Manufacturers')]")))
    driver.find_element_by_id("doc-suppliers").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Suppliers')]")))
    driver.find_element_by_id("doc-delivery_statuses").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Delivery Statuses')]")))
    driver.find_element_by_id("doc-sold_out_statuses").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Sold Out Statuses')]")))
    driver.find_element_by_id("doc-quantity_units").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Quantity Units')]")))
    driver.find_element_by_id("doc-csv").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'CSV Import/Export')]")))
    # Menu Countries
    driver.find_element_by_xpath("//span[contains(text(),'Countries')]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Countries')]")))
    # Menu Currencies
    driver.find_element_by_xpath("//span[contains(text(),'Currencies')]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Currencies')]")))
    # Menu Customers
    driver.find_element_by_xpath("//span[contains(text(),'Customers')]").click()
    driver.find_element_by_id("doc-customers").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Customers')]")))
    driver.find_element_by_id("doc-csv").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'CSV Import/Export')]")))
    driver.find_element_by_id("doc-newsletter").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Newsletter')]")))
    # Menu Geo Zones
    driver.find_element_by_xpath("//span[contains(text(),'Geo Zones')]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Geo Zones')]")))
    # Menu Languages
    driver.find_element_by_xpath("//span[contains(text(),'Languages')]").click()
    driver.find_element_by_id("doc-languages").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Languages')]")))
    driver.find_element_by_id("doc-storage_encoding").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Storage Encoding')]")))
    # Menu Modules
    driver.find_element_by_xpath("//span[contains(text(),'Modules')]").click()
    driver.find_element_by_id("doc-jobs").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Job Modules')]")))
    driver.find_element_by_id("doc-customer").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Customer Modules')]")))
    driver.find_element_by_id("doc-shipping").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Shipping Modules')]")))
    driver.find_element_by_id("doc-payment").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Payment Modules')]")))
    driver.find_element_by_id("doc-order_total").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Order Total Modules')]")))
    driver.find_element_by_id("doc-order_success").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Order Success Modules')]")))
    driver.find_element_by_id("doc-order_action").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Order Action Modules')]")))


    driver.find_element_by_css_selector(".fa.fa-sign-out.fa-lg").click()