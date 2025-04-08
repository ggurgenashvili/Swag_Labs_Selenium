import pytest

from pageObjects.standardUserLogin import StandardUserLogin

def test_userLogin(browserInstance):
    driver = browserInstance
    userLogin = StandardUserLogin(driver)
    print(userLogin.getTitle())
    userLogin.login('standard_user', 'secret_sauce')


