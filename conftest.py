from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene.support.shared import browser
from api import *
from allure import title, step
import pytest
import os
import enviroment_variables


class Capabilities:
    local = "http://127.0.0.1:4723/wd/hub"
    my_device = {
        "platformName": "Android",
        "appium:deviceName": enviroment_variables.device_name,
        "appium:app": f"{os.path.join(os.getcwd(), 'mobile', 'vinteo.apk')}",
        'autoGrantPermissions': enviroment_variables.permissions,
        "appActivity": "com.vinteo.mobile.app.MainActivity",
        "automationName": "uiautomator2",
    }


@title('Подготовка webdriver')
@pytest.fixture(scope='function', autouse=True)
def setup_mobile():
    with step('Настроить соединение'):
        options = UiAutomator2Options().load_capabilities(Capabilities.my_device)
        location = Capabilities.local
        driver = webdriver.Remote(location, options=options)
        browser.config.driver = driver
    yield
    with step('Закрыть соединение'):
        browser.quit()
