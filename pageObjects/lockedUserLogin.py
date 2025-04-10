from selenium.webdriver.common.by import By

from utils.browserutils import BrowserUtils

class lockedUserLogin(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.loginBtn = (By.ID, 'login-button')
        self.errorMsg = (By.CSS_SELECTOR, 'h3[data-test="error"]')


    def login(self, username, password):
        #verify that user is blocked and can't log in into website
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.loginBtn).click()


        login_error = self.driver.find_element(*self.errorMsg)
        assert 'Epic sadface: Sorry, this user has been locked out.' in login_error.text