from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()


#verify that we logged in and header label appears
header_label = driver.find_element(By.CLASS_NAME, 'header_label')
assert 'Swag Labs' in header_label.text
