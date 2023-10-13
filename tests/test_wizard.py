from mobile.model.pages import *
from api import *
from allure import feature, story, suite, title, tag
import pytest


# - Отображение ОШИБКА ПОДКЛЮЧЕНИЯ при регистрации
# - Кнопка ДАЛЕЕ недоступна при вводе невалидного адреса сервера
# - Кнопка ДАЛЕЕ доступна при пустом адресе сервера
# - Ввести в поле ВАШЕ ИМЯ валидные значения
# - Кнопка ДАЛЕЕ недоступна при пустом поле ВАШЕ ИМЯ


@feature('MOBILE')
@story('MOBILE WIZARD')
@suite('Wizard')
@tag('autotests', 'mobile', 'wizard')
@title('Отображение ОШИБКА ПОДКЛЮЧЕНИЯ при регистрации')
@pytest.mark.parametrize('invalid_server_address', ['test.test.test'])
def test_wizard_gives_a_connection_error_during_registration(invalid_server_address):
    """Шаги:
    - Открыть wizard
    - Ввести адрес несуществующего сервера
    - Нажать ДЕЛЕЕ
    - Ждем 20 сек
    - Проверяем отображение Ошибки подключения"""
    WizardPage.type_address_server(address=invalid_server_address)
    WizardPage.click_next_on_address_page(delay=20)
    WizardPage.check_connection_error()


@feature('MOBILE')
@story('MOBILE WIZARD')
@suite('Wizard')
@tag('autotests', 'mobile', 'wizard')
@title('Кнопка ДАЛЕЕ недоступна при вводе невалидного адреса сервера')
@pytest.mark.parametrize('invalid_server_address', ['test', '123', '256.1.0', 'www.'])
def test_wizard_next_button_not_clickable_with_invalid_server_address(invalid_server_address):
    """Шаги:
    - Открыть wizard
    - Ввод невалидного адреса сервера
    - Нажать ДАЛЕЕ
    - Кнопка ДАЛЕЕ не кликабельна, отображается страница настройки сервера"""
    WizardPage.type_address_server(address=invalid_server_address)
    WizardPage.click_next_on_address_page(delay=2)
    assert not(WizardPage.check_open_profile_page()), \
        'Далее доступна для нажатия, открыта страница Заполните свой профиль'


@feature('MOBILE')
@story('MOBILE WIZARD')
@suite('Wizard')
@tag('autotests', 'mobile', 'wizard')
@title('Кнопка ДАЛЕЕ доступна при пустом адресе сервера')
def test_wizard_next_button_available_server_address_is_empty():
    """Шаги:
    - Открыть wizard
    - Оставить пустой АДРЕС СЕРВЕРА
    - Нажать ДАЛЕЕ
    - Отображается страница Настройки сервера"""
    WizardPage.type_address_server(address='')
    WizardPage.click_next_on_address_page(delay=3)
    assert WizardPage.check_open_profile_page(), \
        'ДАЛЕЕ недоступна для нажатия, не удалось открыть страницу Заполните свой профиль'


@feature('MOBILE')
@story('MOBILE WIZARD')
@suite('Wizard')
@tag('autotests', 'mobile', 'wizard')
@title('Ввести {my_name} в поле ВАШЕ ИМЯ')
@pytest.mark.parametrize('my_name', [
    '1',
    'ab',
    'abc',
    'test_test',
    'test/@test',
    'test test',
])
def test_wizard_next_button_available_type_name(my_name):
    """Шаги:
    - Открыть Wizard
    - Оставить пустой АДРЕС СЕРВЕРА
    - Нажать ДАЛЕЕ
    - Ввести ВАШЕ ИМЯ
    - Нажать ДАЛЕЕ
    - Открыта страница Разрешений приложения"""
    WizardPage.type_address_server(address='')
    WizardPage.click_next_on_address_page()
    WizardPage.type_visible_name(my_name)
    WizardPage.click_next_on_the_visible_name_page(delay=2)
    assert WizardPage.check_app_permissions_page_opened(), \
        'ДАЛЕЕ не доступна для нажатия, не удалось открыть страницу' \
        ' Дополнительные разрешения приложения'


@feature('MOBILE')
@story('MOBILE WIZARD')
@suite('Wizard')
@tag('autotests', 'mobile', 'wizard')
@title('Кнопка ДАЛЕЕ недоступна при пустом поле ВАШЕ ИМЯ')
def test_wizard_the_next_button_is_not_available_if_the_your_name_field_is_empty():
    """Шаги:
    - Открыть wizard
    - Ввести адрес сервера
    - Нажать ДАЛЕЕ
    - Ввести ВАШЕ ИМЯ
    - Нажать ДАЛЕЕ
    - Кнопка ДАЛЕЕ недоступна для клика (серая)"""
    WizardPage.type_address_server('')
    WizardPage.click_next_on_address_page()
    WizardPage.type_visible_name('')
    WizardPage.click_next_on_the_visible_name_page(delay=2)
    assert not(WizardPage.check_app_permissions_page_opened()), \
        'Далее доступна для нажатия при пустом поле ВАШЕ ИМЯ, ' \
        'открыта страница Заполните свой профиль'

