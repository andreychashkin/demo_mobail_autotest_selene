from mobile.model.pages import *
from api import *
from allure import feature, story, suite, title, tag
import pytest


# - Добавить контакт в адресную книгу, перебор имен


@feature('MOBILE')
@story('MOBILE CONTACTS')
@suite('Контакты')
@tag('autotests', 'mobile', 'contacts')
@title('Добавить контакт с именем {name} в адресную книгу')
@pytest.mark.parametrize('name', [
    "tests name",
    "Test",
    '123Test',
])
def test_add_contact_name(name):
    """Шаги:
    - Прейти на страницу КОНТАКТЫ
    - Нажать на +
    - В появившимся меню нажать ДОБАВИТЬ КОНТАКТ
    - Ввести имя (разные имена), номер
    - Нажать ГОТОВО
    - Убедиться, что абонент создался"""
    number = '122'
    WizardPage.open_app(visible_name=__name__)
    ContactsPage.add_contact(name=name, number=number)
    ContactsPage.click_contact(number)

