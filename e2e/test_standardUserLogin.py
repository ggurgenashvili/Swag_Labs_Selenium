import json
import os
import sys
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pageObjects.standardUserLogin import StandardUserLogin

test_data_path = '../data/test_standardUserLogin.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data['data']

@pytest.mark.smoke
@pytest.mark.parametrize('test_list_item', test_list)
def test_userLogin(browserInstance, test_list_item):
    driver = browserInstance
    userLogin = StandardUserLogin(driver)
    print(userLogin.getTitle())
    userLogin.login(test_list_item['username'], test_list_item['password'],)


