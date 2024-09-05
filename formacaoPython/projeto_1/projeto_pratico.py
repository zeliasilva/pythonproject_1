from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import pytest

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver

    driver.quit

def test_buysixproducts_withsucess(driver):
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.CLASS_NAME, "submit-button")
    button.click()
    sleep(2)
    
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

    button_add = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
    for button in button_add:
        button.click()
    
    cart_qt= driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")

    assert cart_qt.text == "6"

    sleep(2)

    cart_link = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart_link.click()
    sleep(2)

    remove_button= driver.find_element(By.NAME, "remove-sauce-labs-backpack")
    remove_button.click()

    cart_qt= driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
    
    assert cart_qt.text == "5"
    sleep(2)

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    sleep(2)

    first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
    first_name.send_keys("Maria")

    last_name = driver.find_element(By.NAME, "lastName")
    last_name.send_keys("Silva")

    zip_code = driver.find_element(By.NAME, "postalCode")
    zip_code.send_keys("4501-750")

    continue_button = driver.find_element(By.XPATH, "//input[@name='continue']")
    continue_button.click()
    sleep(5)

    total = 0
    item_price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    for item in item_price:
        total = total + float(item.text.replace("$",""))
    print(total)

    item_total = driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
    assert float(item_total.text.replace("Item total: $","")) == total

    finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish_button.click()

    assert driver.find_element(By.XPATH, "//h2[text()='Thank you for your order!']").text == 'Thank you for your order!'
    sleep(5)

def test_loginfail(driver):
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("error")

    button = driver.find_element(By.CLASS_NAME, "submit-button")
    button.click()
    sleep(5)
    
    assert driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

def test_buy3produts(driver):
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("performance_glitch_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.CLASS_NAME, "submit-button")
    button.click()
    
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

    button_add1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    button_add1.click()

    button_add2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    button_add2.click()

    button_add3 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    button_add3.click()

    cart_qt= driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")

    assert cart_qt.text == "3"

    remove_button= driver.find_element(By.NAME, "remove-sauce-labs-backpack")
    remove_button.click()

    assert cart_qt.text == "2"

    cart_link = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart_link.click()
    sleep(5)

    button_continueshopping = driver.find_element(By.ID, "continue-shopping")
    button_continueshopping.click()
    sleep(2)

    button_add4 = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    button_add4.click()
    sleep(2)

    cart_qt= driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
    assert cart_qt.text == "3"

    cart_link = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart_link.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
    first_name.send_keys("Maria")

    last_name = driver.find_element(By.NAME, "lastName")
    last_name.send_keys("Silva")

    zip_code = driver.find_element(By.NAME, "postalCode")
    zip_code.send_keys("4501-750")

    continue_button = driver.find_element(By.XPATH, "//input[@name='continue']")
    continue_button.click()
    sleep(5)

    finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish_button.click()

    assert driver.find_element(By.XPATH, "//h2[text()='Thank you for your order!']").text == 'Thank you for your order!'
    sleep(5)

    button_bckhome = driver.find_element(By.ID, "back-to-products") 
    button_bckhome.click()

    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
    

def test_cancelshop(driver):
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("performance_glitch_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.CLASS_NAME, "submit-button")
    button.click()
    
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

    see_product = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    see_product.click()

    button_add_produt = driver.find_element(By.ID, "add-to-cart")
    button_add_produt.click()

    cart_qt= driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")

    assert cart_qt.text == "1"

    cart_link = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart_link.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
    first_name.send_keys("Maria")

    last_name = driver.find_element(By.NAME, "lastName")
    last_name.send_keys("Silva")

    zip_code = driver.find_element(By.NAME, "postalCode")
    zip_code.send_keys("4501-750")

    continue_button = driver.find_element(By.XPATH, "//input[@name='continue']")
    continue_button.click()
    
    cancel_button = driver.find_element(By.ID, "cancel")
    cancel_button.click()

    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
