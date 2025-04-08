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


    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.loginBtn).click()
        # verify that we logged in and header label appears
        assert 'Swag Labs' in self.driver.find_element(*self.header).text
