from selenium.webdriver.common.by import By
from pages.mybase_page import BasePage
from time import sleep

#reformular todo o código para novo projecto

class user_data(BasePage):
    FIRST_NAME = (By.XPATH, "//input[@id='input-payment-firstname']")
    LAST_NAME = (By.XPATH, "//input[@id='input-payment-lastname']")
    EMAIL = (By.ID, "input-payment-email")
    PHONE = (By.XPATH, "//input[@id='input-payment-telephone']")
    COMPANY = (By.XPATH, "//input[@id='input-payment-company']")
    ADDRESS_1 = (By.XPATH, "//input[@id='input-payment-address-1']")
    CITY = (By.XPATH, "//input[@id='input-payment-city']")
    POSTCODE = (By.XPATH, "//input[@id='input-payment-postcode']")
    TERMS = (By.XPATH, "//label[@class='custom-control-label' and @for='input-agree']")
    # CONTINUE_BUTTON = (By.XPATH, "//button[@id='button-save']")
    CONTINUE_BUTTON = (By.XPATH, '//button[text()="Continue "]')

    def fill_user_data(self, first_name, last_name, email, phone, company, address_1, city, postcode):
        self.wait_for_element(self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PHONE).send_keys(phone)
        self.driver.find_element(*self.COMPANY).send_keys(company)
        self.driver.find_element(*self.ADDRESS_1).send_keys(address_1)
        self.driver.find_element(*self.CITY).send_keys(city)
        self.driver.find_element(*self.POSTCODE).send_keys(postcode)
        sleep(3)
        self.driver.find_element(*self.TERMS).click()
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def fill_first_name(self, first_name):
        self.wait_for_element(self.FIRST_NAME).send_keys(first_name)
    
    def fill_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
    
    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def fill_phone(self, phone):
        self.driver.find_element(*self.PHONE).send_keys(phone)

    def fill_company(self, company):
        self.driver.find_element(*self.COMPANY).send_keys(company)
    
    def fill_address_1(self, address_1):
        self.driver.find_element(*self.ADDRESS_1).send_keys(address_1)

    def fill_city(self, city):
        self.driver.find_element(*self.CITY).send_keys(city)

    def fill_postcode(self, postcode):
        self.driver.find_element(*self.POSTCODE).send_keys(postcode)

    def click_accept_terms(self):
        self.driver.find_element(*self.TERMS).click()

    def click_continue_button(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
    sleep(5)