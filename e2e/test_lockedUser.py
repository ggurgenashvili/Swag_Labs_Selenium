from pageObjects.lockedUserLogin import lockedUserLogin


def test_locked_user(browserInstance):
    driver = browserInstance
    userLogin = lockedUserLogin(driver)
    userLogin.login('locked_out_user', 'secret_sauce')