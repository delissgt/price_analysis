import re

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://tienda.makro.com.co/ca/despensa/aceites/oliva/CP_12/CP_12_01/CP_12_01_01')

store_url_product = "https://tienda.makro.com.co/p/"
pattern_ean = r'(\d{6})'

sleep(40)


my_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".card-product-vertical.product-card-default")


for element in my_elements:

    product_name = element.find_element(by=By.CSS_SELECTOR, value=".CardName__CardNameStyles-sc-147zxke-0.bWeSzf.prod__name")
    print("product_name::::::", product_name.text)

    product_price = element.find_element(by=By.CSS_SELECTOR, value=".CardBasePrice__CardBasePriceStyles-sc-1dlx87w-0.bhSKFL.base__price")
    print("product_price::::::", product_price.text)

    product_url_img = element.find_element(by=By.TAG_NAME, value="img").get_attribute("src")
    print("product_url_img::::::", product_url_img)

    product_ean: int = 000000
    product_url: str = ""

    if product_url_img != "https://makro.com.co/imagesProducts/medias/134156_500X500_ON_100000000.png?":
        product_ean = int(re.findall(pattern_ean, product_url_img)[0])
        product_url = store_url_product + str(product_ean)

    print("product_EAN::::::", product_ean)
    print("product_url::::::", product_url)

    print("----------------------")

