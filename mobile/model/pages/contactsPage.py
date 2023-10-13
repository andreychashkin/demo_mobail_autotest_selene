from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
import time
from allure import step


class ContactsPage:

    @staticmethod
    @step('Нажать КОНТАКТЫ (открыть адресную книгу)')
    def open_contacts(delay=0) -> None:
        """Метод открывает меню контакты"""
        browser.element((AppiumBy.ACCESSIBILITY_ID,
                         'tab_bar.contacts_label')).click()
        time.sleep(delay)
        
    @staticmethod
    @step('Нажать ПЛЮС в меню контакты')
    def click_plus_button_in_contacts(delay=0) -> None:
        """Нажимаем + в меню контакты"""
        browser.element((AppiumBy.ACCESSIBILITY_ID,
                         'contacts_screen.header.plus_icon')).click()
        time.sleep(delay)

    @staticmethod
    @step('Нажать ДОБАВИТЬ КОНТАКТ')
    def click_add_contact_in_modal(delay=0) -> None:
        """Нажимаем ДОБАВИТЬ КОНТАКТ в модальном окне"""
        browser.element((AppiumBy.ACCESSIBILITY_ID,
                         'contacts_screen.modal_add_contact')).click()
        time.sleep(delay)


    @staticmethod
    @step('Добавить контакт в адресную книгу')
    def add_contact(name: str, number: str, mail: str = None) -> None:
        """Добавляем контакт в адресную книгу"""
        ContactsPage.open_contacts()
        ContactsPage.click_plus_button_in_contacts()
        ContactsPage.click_add_contact_in_modal()
        ContactsPage.contact_name_input(name)
        ContactsPage.contact_number_input(number)
        if mail:
            ContactsPage.contact_mail_input(mail)
        ContactsPage.click_done_button_contact()


    @staticmethod
    @step("Заполнить поле НОМЕР")
    def contact_number_input(number: str, delay=0) -> None:
        """Вводим номер контакта"""
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'add_contact_screen.number_section.input')).type(number)
        time.sleep(delay)

    @staticmethod
    @step("Заполнить поле ИМЯ")
    def contact_name_input(name: str) -> None:
        """Вводим имя контакта"""
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'add_contact_screen.name_section.input')).type(name)

    @staticmethod
    @step("Заполнить поле EMAIL")
    def contact_mail_input(mail: str) -> None:
        """Вводим эл. почту контакта"""
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'add_contact_screen.email_section.input')).type(mail)

    @staticmethod
    @step("Нажать ГОТОВО")
    def click_done_button_contact(delay=0) -> None:
        """Нажимаем кнопку готово"""
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'add_contact_screen.done_button')).click()
        time.sleep(delay)
        
    @staticmethod
    @step("Нажать на контакт в адресной книге")
    def click_contact(number, delay=0) -> None:
        """Кликаем по контакту в адресной книге"""
        browser.element((AppiumBy.XPATH,
                         f'(//android.view.ViewGroup[@content-desc="contacts_screen.contact_item"])'
                         f'/*[@text="{number}"]')).click()
        time.sleep(delay)
