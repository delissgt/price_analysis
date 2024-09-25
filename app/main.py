from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# driver.get('https://google.com')
driver.get('https://tienda.makro.com.co/ca/despensa/aceites/oliva/CP_12/CP_12_01/CP_12_01_01')
sleep(25)

# my_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".card-product-vertical.product-card-default")
my_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".card-product-vertical.product-card-default")
# [<selenium.webdriver.remote.webelement.WebElement (session="e5dc7d0dfeff67127376ab02bf790fb0", element="f.2CCED3CB86B934F407A17AC01FA8BE17.d.B4221124B7E759A3C74396791A59DE73.e.33")>,


for element in my_elements:
    # product_name = element.find_elements(By.CSS_SELECTOR, ".CardName__CardNameStyles-sc-147zxke-0 bWeSzf prod__name")
    # print("product_name:", product_name)
    # product_name = driver.find_element(by=By.CSS_SELECTOR, value=".CardName__CardNameStyles-sc-147zxke-0.bWeSzf.prod__name")

    product_name = element.find_element(by=By.CSS_SELECTOR, value=".CardName__CardNameStyles-sc-147zxke-0.bWeSzf.prod__name")
    print("product_name::::::", product_name.text)

    product_price = element.find_element(by=By.CSS_SELECTOR, value=".CardBasePrice__CardBasePriceStyles-sc-1dlx87w-0.bhSKFL.base__price")
    print("product_price::::::", product_price.text)

    # product_url_img = element.find_element(by=By.CLASS_NAME, value="prod__figure__img").get_attribute("src")
    # product_url_img = element.find_element(by=By.CLASS_NAME, value="prod__figure__img")
    print(element.get_attribute('innerHTML'))
    product_url_img = element.find_element(by=By.TAG_NAME, value="img").get_attribute("src")
    print("product_url_img::::::", product_url_img)
    # print(element)

# todo https://tienda.makro.com.co/p/112763
#  url + 112763
# number = EAN product --> obtain from image

