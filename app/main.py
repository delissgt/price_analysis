import re
from selenium.common.exceptions import NoSuchElementException
from db import insert_product
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://tienda.makro.com.co/ca/despensa/aceites/oliva/CP_12/CP_12_01/CP_12_01_01')

store_url_product = "https://tienda.makro.com.co/p/"
pattern_ean = r'(\d{6})'

sleep(70)


my_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".card-product-vertical.product-card-default")


for element in my_elements:

    try:

        product_name = element.find_element(by=By.CSS_SELECTOR, value=".CardName__CardNameStyles-sc-147zxke-0.bWeSzf.prod__name").text

        full_price = element.find_element(by=By.CSS_SELECTOR, value=".CardBasePrice__CardBasePriceStyles-sc-1dlx87w-0.bhSKFL.base__price")
        full_price = float(re.sub(r'[^\w]', '', full_price.text))

        discount_price = element.find_element(by=By.CLASS_NAME, value="base__price")
        discount_price = float(re.sub(r'[^\w]', '', discount_price.text))

        product_url_img = element.find_element(by=By.TAG_NAME, value="img").get_attribute("src")

        product_ean: int = 000000
        product_url: str = ""

        if product_url_img != "https://makro.com.co/imagesProducts/medias/134156_500X500_ON_100000000.png?":
            product_ean = int(re.findall(pattern_ean, product_url_img)[0])
            product_url = store_url_product + str(product_ean)

        insert_product(product_name, product_ean, full_price, discount_price, product_url, product_url_img)
    except NoSuchElementException:
        pass

