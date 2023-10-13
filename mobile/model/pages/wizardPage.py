from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene.support.conditions import have, be
import time
from allure import step


class WizardPage:

    @staticmethod
    @step('Пройти первоначальную настройку приложения')
    def open_app(server_address='demo.vinteo.com', visible_name='Mobile') -> None:
        """Метод принимает на вход адрес сервера регистрации и имя пользователя"""
        try:
            WizardPage.type_address_server(server_address)
            WizardPage.click_next_on_address_page()
            WizardPage.type_visible_name(visible_name=visible_name)
            WizardPage.click_next_on_the_visible_name_page()
            WizardPage.click_on_done_on_the_app_permission()
        except:
            return None

    @staticmethod
    @step('Заполнить поле АДРЕС СЕРВЕРА')
    def type_address_server(address: str = 'demo.vinteo.com', delay=0) -> None:
        """Ввести адрес сервера"""
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'onboarding_server_screen.server_input')).type(address)
        time.sleep(delay)

    @staticmethod
    @step('Нажать ДАЛЕЕ на странице адрес сервера')
    def click_next_on_address_page(delay=0) -> None:
        """Клик по кнопке Далее на странице введите адрес сервера Wizard"""
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'onboarding_server_screen.continue_button')).click()
        time.sleep(delay)

    @staticmethod
    @step('Заполнить поле ОТОБРАЖАЕМОЕ ИМЯ')
    def type_visible_name(visible_name: str, delay=0) -> None:
        """Ввод ВАШЕ ИМЯ в Wizard"""
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'onboarding_profile_screen.user_name_input')).type(visible_name)
        time.sleep(delay)

    @staticmethod
    @step('Нажать ДАЛЕЕ на странице Заполните свой профиль')
    def click_next_on_the_visible_name_page(delay=0) -> None:
        """Клик ДАЛЕЕ на странице Заполните свой профиль"""
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'onboarding_profile_screen.done_button')).click()
        time.sleep(delay)

    @staticmethod
    @step('Нажать ГОТОВО на странице Разрешения приложения')
    def click_on_done_on_the_app_permission(delay=0) -> None:
        """Клик ГОТОВО на странице Разрешения приложения"""
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'onboarding_permissions_screen.done_button')).click()
        time.sleep(delay)

    @staticmethod
    @step('Ожидаемый результат: Ошибка - ОШИБКА ПОДКЛЮЧЕНИЯ')
    def check_connection_error() -> None:
        """Проверяем отображение Ошибки - ОШИБКА ПОДКЛЮЧЕНИЯ"""
        assert browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout')).should(be.visible), \
               'Алерт ОШИБКА ПОДКЛЮЧЕНИЯ не отображается на странице'
        assert browser.element((AppiumBy.ID, 'android:id/alertTitle')).should(have.text('Ошибка подключения')), \
               'Title отличается от ОШИБКА ПОДКЛЮЧЕНИЯ'
        assert browser.element((AppiumBy.ID, 'android:id/message')).\
               should(have.text('Проверьте адрес сервера и подключение к Интернету: Network Error')),\
               'Текст ошибки не содержит -- Проверьте адрес сервера и подключение к Интернету: Network Error --'

    @staticmethod
    @step('Ожидаемый результат: открыта страницы ЗАПОЛНИТЕ СВОЙ ПРОФИЛЬ')
    def check_open_profile_page():
        """Проверка открытия страницы Заполните свой профиль"""
        return browser.element((AppiumBy.ACCESSIBILITY_ID, 'onboarding_profile_screen.user_name_input')).\
            is_displayed()

    @staticmethod
    @step('Ожидаемый результат: открыта страница РАЗРЕШЕНИЯ ПРИЛОЖЕНИЯ')
    def check_app_permissions_page_opened():
        """Проверка открытия страницы Разрешений приложения"""
        return not(browser.element((AppiumBy.ACCESSIBILITY_ID, 'onboarding_profile_screen.user_name_input')). \
            is_displayed())

    @staticmethod
    @step('Загрузить аватар')
    def upload_avatar() -> None:
        """Загрузка аватарки через фото"""
        browser.element((AppiumBy.XPATH,
                         '//android.view.ViewGroup[@content-desc="onboarding_profile_screen.camera_button"]'
                         '/android.view.ViewGroup')).type('./test_avatar.jpeg')

    @staticmethod
    @step('Нажать ПОКАЗАТЬ УВЕДОМЛЕНИЯ')
    def click_show_notifications(delay=0) -> None:
        """Клик ПОКАЗАТЬ УВЕДОМЛЕНИЯ"""
        browser.element((AppiumBy.ACCESSIBILITY_ID,
                         'onboarding_permissions_screen.android_show_notifications_item')).click()
        time.sleep(delay)
