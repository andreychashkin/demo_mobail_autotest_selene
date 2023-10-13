from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene import be, have

import time
from allure import step


class CallPage:
    
    @staticmethod
    @step('Ожидаемый результат: клиент подключен к конференции')
    def check_call_complete(delay=0) -> None:
        """Метод проверяет что на экране отображается видео"""
        assert browser.element((AppiumBy.XPATH,
                                '//android.view.View')).should(be.visible), 'Элемент отображающий видео не найден'
        time.sleep(delay)
    
    @staticmethod
    @step('Ожидаемый результат: отображается введенный номер')
    def check_number(number: str, delay=0) -> None:
        """Метод проверяет введенный номер"""
        browser.element((AppiumBy.XPATH,
                         '//android.view.ViewGroup/android.widget.HorizontalScrollView/'
                         'android.view.ViewGroup/android.widget.TextView')).should(have.text(number))
        time.sleep(delay)
    
    @staticmethod
    @step('Нажать НАМПАД')
    def click_numpad_button(delay=0) -> None:
        """Метод открывает нампад"""
        browser.element((AppiumBy.ACCESSIBILITY_ID,
                         'recents_screen.numpad_button')).click()
        time.sleep(delay)

    @staticmethod
    @step('Ввести номер нажаием кнопок в НАМПАД')
    def click_number(number: [], delay=0) -> None:
        """Метод принимает на вход кнопку, которую хотим нажать на нампаде 1-9, . @, для точки нужно передать point"""
        for i in number:
            browser.element((AppiumBy.ACCESSIBILITY_ID,
                             f'numpad.button_{i}')).click()

        time.sleep(delay)

    @staticmethod
    @step('Нажать ВЫЗОВ')
    def click_phone_call(delay=0) -> None:
        """Метод на кнопку вызова"""
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'phone_button')).click()
        time.sleep(delay)

    @staticmethod
    @step('Нажать КЛАВИАТУРА в меню набора номера')
    def click_keyboard_button(delay=0) -> None:
        """Метод нажимает на кнопку КЛАВИАТУРА в меню набора номера"""
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'numpad_screen.keyboard_botton')).click()
        time.sleep(delay)

    @staticmethod
    @step('Ввести номер с КЛАВИАТУРЫ')
    def input_number_with_keyboard(number: str, delay=0) -> None:
        """Вводим НОМЕР с использованием КЛАВИАТУРЫ в меню набора номера"""
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'numpad_screen.text_input')).type(number)
        time.sleep(delay)

    @staticmethod
    def type_number_and_call(number: str, delay=15) -> None:
        """Выполняем вызов"""
        CallPage.click_keyboard_button()
        CallPage.input_number_with_keyboard(number)
        CallPage.click_keyboard_button()
        CallPage.click_phone_call(delay=2)
        time.sleep(delay)


