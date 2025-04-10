from selenium.webdriver.common.by import By

from utils.browserutils import BrowserUtils


class StandardUserLogin(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.loginBtn = (By.ID, 'login-button')
        self.header = (By.CLASS_NAME, 'header_label')

        self.addToCart = (By.TAG_NAME, 'button')
        self.shopCartCont = (By.ID, 'shopping_cart_container')
        self.checkOutBtn = (By.ID, 'checkout')
        self.firstName_input = (By.ID, 'first-name')
        self.lastName_input = (By.ID, 'last-name')
        self.zipCode = (By.ID, 'postal-code')
        self.contBtn = (By.ID, 'continue')
        self.finishBtn = (By.ID, 'finish')
        self.backToProductsBtn = (By.ID, 'back-to-products')
        self.products_header = (By.CLASS_NAME, 'header_secondary_container')

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.loginBtn).click()
        # verify that we logged in and header label appears
        assert 'Swag Labs' in self.driver.find_element(*self.header).text

    def checkOut(self, firstName, lastName, zipCode):
        buttons = self.driver.find_elements(*self.addToCart)
        buttons[2].click()
        self.driver.find_element(*self.shopCartCont).click()
        self.driver.find_element(*self.checkOutBtn).click()
        self.driver.find_element(*self.firstName_input).send_keys(firstName)
        self.driver.find_element(*self.lastName_input).send_keys(lastName)
        self.driver.find_element(*self.zipCode).send_keys(zipCode)
        self.driver.find_element(*self.contBtn).click()
        self.driver.find_element(*self.finishBtn).click()
        self.driver.find_element(*self.backToProductsBtn).click()
        #verify that we are back on products page
        assert 'Products' in self.driver.find_element(*self.products_header).text