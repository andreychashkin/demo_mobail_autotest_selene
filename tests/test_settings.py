from mobile.model.pages import *
from api import *
from allure import feature, story, suite, title, tag
import pytest


# - Авторизация на сервере через настройки


@feature('MOBILE')
@story('MOBILE SETTINGS')
@suite('Настройки')
@tag('autotests', 'mobile', 'settings')
@title('Авторизовать клиент на сервере')
def test_authorization_on_the_server():
    """Шаги:
    - Перейти на страницу Настройки
    - Нажать на поле Настройки сервера
    - Ввести адрес сервера
    - Нажать ГОТОВО
    - Убедиться что адрес сервера отображается корректно"""
    WizardPage.open_app(visible_name=__name__)
    SettingsPage.open_settings()
    SettingsPage.input_registered(address='demo.vinteo.com')
    SettingsPage.click_on_the_done_button_in_settings_server()

