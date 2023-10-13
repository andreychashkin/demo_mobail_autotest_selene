from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
import time
from allure import step


class SettingsPage:

    @staticmethod
    @step('Нажать НАСТРОЙКИ (Шестеренка)')
    def open_settings(delay=0) -> None:
        """Метод открывает настройки приложения / клик по иконке Шестеренка"""
        browser.element((AppiumBy.ACCESSIBILITY_ID,
                         'tab_bar.settings_label')).click()
        time.sleep(delay)

    @staticmethod
    @step("Зарегистрироваться согласно введенным данным")
    def input_registered(address: str,
                         authorization: bool = False,
                         login: str | None = None,
                         password: str | None = None,
                         delay=20) -> None:
        """Открываем окно регистрации и вводим данные с сохранением настроек"""
        SettingsPage.click_on_the_server_settings_button()
        SettingsPage.clear_and_type_server_address(address=address)
        if authorization:
            SettingsPage.click_authorization_switch()
            SettingsPage.clear_and_type_login(login=login)
            SettingsPage.clear_and_type_password(password=password)
            SettingsPage.click_on_the_done_button_in_settings_server()
        time.sleep(delay)

    @staticmethod
    @step('Нажать по НАСТРОЙКИ СЕРВЕРА')
    def click_on_the_server_settings_button(delay=0) -> None:
        """Клик по кнопке НАСТРОЙКИ СЕРВЕРА"""
        browser.element((AppiumBy.ACCESSIBILITY_ID,
                         'settings_screen.authorization_button')).click()
        time.sleep(delay)
        
    @staticmethod
    @step('Заполнить поле АДРЕС СЕРВЕРА')
    def clear_and_type_server_address(address: str, delay=0) -> None:
        """Очищаем и вводим данные в поле Адрес сервера"""
        browser.element((AppiumBy.ACCESSIBILITY_ID,
                         'authorization_screen.server_input')).clear().type(address)
        time.sleep(delay)
        
    @staticmethod
    @step('Нажать по ВКЛЮЧИТЬ/ОТКЛЮЧИТЬ АВТОРИЗАЦИЮ')
    def click_authorization_switch(delay=0) -> None:
        """Кликаем на переключатель авторизации"""
        browser.element((AppiumBy.ACCESSIBILITY_ID,
                         'authorization_screen.authorization_section.switch_button')).click()
        time.sleep(delay)

    @staticmethod
    @step('Заполнить поле ЛОГИН')
    def clear_and_type_login(login: str, delay=0) -> None:
        """Очищаем и вводим ЛОГИН"""
        browser.element((AppiumBy.ACCESSIBILITY_ID,
                         'authorization_screen.username_input')).clear().type(login)
        time.sleep(delay)

    @staticmethod
    @step('Заполнить поле ПАРОЛЬ')
    def clear_and_type_password(password: str, delay=0) -> None:
        """Очищаем и вводим ПАРОЛЬ"""
        browser.element((AppiumBy.ACCESSIBILITY_ID,
                         'authorization_screen.password_input')).clear().type(password)
        time.sleep(delay)

    @staticmethod
    @step('Нажать ГОТОВО в окне авторизации')
    def click_on_the_done_button_in_settings_server(delay=0) -> None:
        """Клик по кнопке ГОТОВО в окне авторизации"""
        browser.element((AppiumBy.XPATH,
                         '//android.view.ViewGroup[@content-desc="authorization_screen.header.right_button"]'
                         '/android.widget.TextView')).click()
        time.sleep(delay)
