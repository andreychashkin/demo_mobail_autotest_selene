from mobile.model.pages import *
from api import *
from allure import feature, story, suite, title, tag
import pytest

# - Набрать номер через НАМПАД
# - Ввод номера через клавиатуру и вызов


@feature('MOBILE')
@story('MOBILE CALLS')
@suite('Вызовы')
@tag('autotests', 'mobile', 'calls')
@title('Набрать номер через нампад')
def test_input_number():
    """Шаги:
        - Нажать НАМПАД
        - Ввести номер
        - Убедиться что номер отображается"""
    WizardPage.open_app(visible_name=__name__)
    CallPage.click_numpad_button()
    CallPage.click_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 'point', 0, '@'])
    CallPage.check_number('123456789.0@')


@feature('MOBILE')
@story('MOBILE CALLS')
@suite('Вызовы')
@tag('autotests', 'mobile', 'calls')
@title('Набрать номер {number} через клавиатуру и выполнить вызов')
@pytest.mark.parametrize('number', ['@demo.vinteo.com'])
def test_input_number_and_call(number):
    """Шаги:
        - Нажать НАМПАД
        - Нажать КЛАВИАТУРА
        - Ввести номер
        - Нажать КЛАВИАТУРА,чтобы закрыть ввод
        - Нажать ВЫЗОВ
        - Убедиться что отображается контент в звонке"""
    conf = '45231' # тут должна быть передача номера существующей конференции - создание в фикстуре при помощи апи
    conf_number = conf + number
    WizardPage.open_app(visible_name=__name__)
    CallPage.click_numpad_button()
    CallPage.type_number_and_call(conf_number)
    CallPage.check_call_complete()
    
