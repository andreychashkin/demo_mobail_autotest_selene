from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
import time
from allure import step


model = 'PIXEL3'# 'HONOR', 'PIXEL3'
# locators
permission_allow = { # клик РАЗРЕШИТЬ в системном алерте
        'XIAOMI': 'com.android.permissioncontroller:id/permission_allow_button',
        'HONOR': 'com.android.permissioncontroller:id/permission_allow_button',
        'PIXEL3': 'com.android.permissioncontroller:id/permission_allow_button'}
permission_video_or_audio = { # клик РАЗРЕШИТЬ ВО ВРЕМЯ ИСПОЛЬЗОВАНИЯ ПРИЛОЖЕНИЯ
        'XIAOMI': 'com.android.permissioncontroller:id/permission_allow_foreground_only_button', 
        'HONOR': 'com.android.permissioncontroller:id/permission_allow_button',
        'PIXEL3': 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'}


class SystemPage:

    @staticmethod
    @step('Нажать РАЗРЕШИТЬ в системном алерте')
    def click_allow_button(delay=2) -> None:
        """Клик РАЗРЕШИТЬ в системном алерте"""
        browser.element((AppiumBy.ID,
                         permission_allow[model])).click()
        time.sleep(delay)

    @staticmethod
    @step('Нажать РАЗРЕШИТЬ ВО ВРЕМЯ ИСПОЛЬЗОВАНИЯ ПРИЛОЖЕНИЯ аудио или видео в системном алерте')
    def click_allow_button_video_or_audio_permission(delay=2) -> None:
        """Клик РАЗРЕШИТЬ ВО ВРЕМЯ ИСПОЛЬЗОВАНИЯ ПРИЛОЖЕНИЯ аудио или видео"""
        browser.element((AppiumBy.ID,
                     permission_video_or_audio[model])).click()
        time.sleep(delay)

    @staticmethod
    @step('Нажать РАЗРЕШИТЬ презентацию в системном алерте')
    def click_allow_sharing_button(delay=2) -> None:
        """Клик РАЗРЕШИТЬ презентацию в системном алерте"""
        browser.element((AppiumBy.ID,
                         'android:id/button1')).click()
        time.sleep(delay)


    @staticmethod
    @step('Нажать ЗАПРЕТИТЬ в системном алерте')
    def click_deny_button(delay=2) -> None:
        """Клик ЗАПРЕТИТЬ в системном алерте"""
        browser.element((AppiumBy.ID,
                         'com.android.permissioncontroller:id/permission_deny_button')).click()
        time.sleep(delay)

    @staticmethod
    @step('Получить текст уведомления (permission)')
    def get_system_alert_text() -> str:
        """Получить текст уведомления (permission)"""
        return browser.element((AppiumBy.ID,
                                'com.android.permissioncontroller:id/permission_message')).get_attribute('text')

    @staticmethod
    @step('Проверить отображение системного алерта')
    def check_show_system_alert() -> bool:
        """Проверка отображения системного алерта"""
        return browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/grant_dialog')).is_displayed()
