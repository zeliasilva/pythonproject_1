from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.mybase_page import BasePage
from pages.user_data_page import user_data
#from pages.step2_page import Etapa2Page
#from pages.step3_page import Etapa3Page
#from pages.last_page import FinalPage

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    
    BasePage(driver).open_site()

    yield driver

    driver.quit()

def test_buy_without_login(driver):
    dropdown_mega_menu = driver.find_element(By.XPATH, "//span[contains(text(),'Mega Menu')]")
    asus_option= driver.find_element(By.XPATH, "//a[@title='Asus']")

    actions = ActionChains(driver)
    actions.move_to_element(dropdown_mega_menu)
    actions.perform()
    asus_option.click()

    first_product = driver.find_element(By.XPATH, "(//img[@title='Canon EOS 5D'])[7]")
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(first_product)
    )
    first_product.click()

    # Esperar até que o dropdown esteja presente
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='input-option238-216836']"))
    )
    sleep(2)
    # Criar um objeto Select
    select = Select(dropdown)
    sleep(2)
    # Selecionar o primeiro elemento (índice 0)
    select.select_by_index(1)  # 1 para "Small (+$48.00)", já que o índice 0 é a opção padrão
    sleep(2)

    increase_qt = driver.find_element(By.XPATH, "(//button[@aria-label='Increase quantity'])[2]")
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(increase_qt)
    )
    increase_qt.click()
    
    add_cart_button = driver.find_element(By.XPATH, "(//button[@title='Add to Cart'])[2]")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(add_cart_button)
    )
    add_cart_button.click()

    cart_qt = driver.find_element(By.XPATH, "//span[@class='badge badge-pill badge-info cart-item-total']")
    sleep(4)

    assert cart_qt.text == "2"

    checkout_cart = driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-block']")
    checkout_cart.click()
    sleep(5)
    edit_qt = driver.find_element(By.XPATH, "(//input[@class='form-control'])[1]")
    
    edit_qt.click()
    edit_qt.clear()
    edit_qt.send_keys('1')

    update_qt = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-primary[data-toggle="tooltip"]'))
    )
    update_qt.click()

    checkout_button = driver.find_element(By.XPATH, "//a[@class='btn btn-lg btn-primary']")
    checkout_button.click()

    sleep(3)
    select_guest = driver.find_element(By.XPATH, "//label[@for='input-account-guest']")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(select_guest)
    )
    select_guest.click()

    fill_data = user_data(driver)
    fill_data.fill_user_data("Zélia", "Silva", "licas-silva@hotmail.com", "+3519998877", "Empresa1","Rua do teste", "Porto","4450-457")

    # Esperar até que o dropdown countries esteja presente
    dropdown_countries = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='input-payment-country']"))
    )
    # Criar um objeto Select
    select = Select(dropdown_countries)
    select.select_by_visible_text('Portugal') 

    # Esperar até que o dropdown cities esteja presente
    dropdown_cities = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='input-payment-zone']"))
    )
    # Criar um objeto Select
    select = Select(dropdown_cities)
    sleep(3)
    select.select_by_visible_text('Porto')  

    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Continue "]'))
    )
    continue_button.click()

    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='button-confirm']"))
    )
    confirm_button.click()

    sucess_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[@class='page-title my-3']"))
    )

    assert sucess_message.text == "Your order has been placed!"














