import pytest

from selenium import webdriver

from pages.auth_page import AuthPage

from settings import valid_email, valid_password, valid_reg_email, valid_reg_password

from settings import (nonvalid_password, nonvalid_email,unformatted_email,
                       one_character_password, four_character_password, five_character_password)

from settings import empty_password, empty_email


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()



class TestAuthPositive:

# Тест-кейс EXC-001 "Авторизация пользователя по валидным значениям адреса электронной почты и пароля"

    def test_positive_authorisation_by_valid_email_and_password(self, driver):
        page = AuthPage(driver)
        page.enter_email(text=valid_email)
        page.enter_password(text=valid_password)
        page.click_login_btn()
        assert page.get_auth_page() == 'https://excursium.com/Account/Dashboard'


class TestAuthNegative:

# Тест-кейс EXC-002 "Авторизация по пустым значениям адреса электронной почты и пароля"

    def test_negative_authorisation_by_empty_email_and_password(self, driver):
        page = AuthPage(driver)
        page.enter_email(text=empty_email)
        page.enter_password(text=empty_password)
        page.click_login_btn()
        assert page.get_auth_page() == 'https://excursium.com/Client/Login'

# Тест-кейс EXC-003 "Авторизация по валидному значению адреса электронной почты и пустому паролю"

    def test_negative_authorisation_by_valid_email_and_empty_password(self, driver):
        page = AuthPage(driver)
        page.enter_email(text=valid_email)
        page.enter_password(text=empty_password)
        page.click_login_btn()
        assert page.get_auth_page() == 'https://excursium.com/Client/Login'

# Тест-кейс EXC-004 "Авторизация по пустому значению адреса электронной почты и валидному паролю"

    def test_negative_authorisation_by_empty_email_and_valid_password(self, driver):
        page = AuthPage(driver)
        page.enter_email(text=empty_email)
        page.enter_password(text=valid_password)
        page.click_login_btn()
        assert page.get_auth_page() == 'https://excursium.com/Client/Login'

# Тест-кейс EXC-005 "Авторизация по валидному значению адреса электронной почты и невалидному паролю"

    def test_negative_authorisation_by_valid_email_and_nonvalid_password(self, driver):
        page = AuthPage(driver)
        page.enter_email(text=valid_email)
        page.enter_password(text=nonvalid_password)
        page.click_login_btn()
        assert page.get_auth_page() == 'https://excursium.com/Client/Login'

# Тест-кейс EXC-006 "Авторизация по невалидному значению адреса электронной почты и валидному паролю"

    def test_negative_authorisation_by_nonvalid_email_and_valid_password(self, driver):
        page = AuthPage(driver)
        page.enter_email(text=nonvalid_email)
        page.enter_password(text=valid_password)
        page.click_login_btn()
        assert page.get_auth_page() == 'https://excursium.com/Client/Login'


# Тест-кейс EXC-007 "Авторизация по невалидным значениям адреса электронной почты и пароля"

    def test_negative_authorisation_by_nonvalid_email_and_nonvalid_password(self, driver):
        page = AuthPage(driver)
        page.enter_email(text=nonvalid_email)
        page.enter_password(text=nonvalid_password)
        page.click_login_btn()
        assert page.get_auth_page() == 'https://excursium.com/Client/Login'

# Тест-кейс EXC-008 "Авторизация по неформатному значению адреса электронной почты и валидному паролю"

    def test_negative_authorisation_by_unformatted_email_and_valid_password(self, driver):
        page = AuthPage(driver)
        page.enter_email(text=unformatted_email)
        page.enter_password(text=valid_password)
        page.click_login_btn()
        assert page.get_auth_page() == 'https://excursium.com/Client/Login'


class TestNavigationAndLinks:

# Тест-кейс EXC-009 "Переход к регистрации"

    def test_positive_transition_page_registration(self, driver):
        page = AuthPage(driver)
        page.click_registration_btn()
        assert page.is_registration_tab_active() == True

# Тест-кейс EXC-010 "Переход к восстановлению пароля"

    def test_positive_transition_page_password_recovery(self, driver):
        page = AuthPage(driver)
        page.click_forgot_password_btn()
        assert page.is_recovery_mode_active()


class TestRegistrationPositive:

# Тест-кейс EXC-011 "Регистрация пользователя при помощи валидных значений адреса электронной почты и пароля"

    def test_positive_registration_by_valid_email_and_password(self, driver):
        page = AuthPage(driver)
        page.click_registration_btn()
        page.enter_reg_email(text=valid_reg_email)
        page.enter_reg_password(text=valid_reg_password)
        page.click_checkbox()
        page.click_creating_account_btn()
        assert page.is_confirm_visible() == True


class TestRegistrationNegative:

# Тест-кейс EXC-012 "Регистрация уже зарегистрированного пользователя"

    def test_negative_registration_by_already_registered_email(self, driver):
        page = AuthPage(driver)
        page.click_registration_btn()
        page.enter_reg_email(text=valid_email)
        page.enter_reg_password(text=valid_password)
        page.click_checkbox()
        page.click_creating_account_btn()
        assert page.get_auth_page() == 'https://excursium.com/Client/Login'

# Тест-кейс EXC-014 "Регистрация с паролем, содержащим 1 символ"

    def test_negative_registration_by_single_character_password(self, driver):
        page = AuthPage(driver)
        page.click_registration_btn()
        page.enter_reg_email(text=valid_reg_email)
        page.enter_reg_password(text=one_character_password)
        page.click_checkbox()
        page.click_creating_account_btn()
        assert page.get_auth_page() == 'https://excursium.com/Client/Login'

# Тест-кейс EXC-015 "Регистрация с паролем, содержащим 4 символа"

    def test_negative_registration_by_four_character_password(self, driver):
        page = AuthPage(driver)
        page.click_registration_btn()
        page.enter_reg_email(text=valid_reg_email)
        page.enter_reg_password(text=four_character_password)
        page.click_checkbox()
        page.click_creating_account_btn()
        assert page.get_auth_page() == 'https://excursium.com/Client/Login'

# Тест-кейс EXC-016 "Регистрация с паролем, содержащим 5 символов"

    def test_positive_registration_by_five_character_password(self, driver):
        page = AuthPage(driver)
        page.click_registration_btn()
        page.enter_reg_email(text=valid_reg_email)
        page.enter_reg_password(text=five_character_password)
        page.click_checkbox()
        page.click_creating_account_btn()
        assert page.get_auth_page() == 'https://excursium.com/Client/Login'

# Тест-кейс EXC-017 "Регистрация с валидным адресом электронной почты и пустому значению пароля"

    def test_negative_registration_by_valid_email_and_empty_password(self, driver):
        page = AuthPage(driver)
        page.click_registration_btn()
        page.enter_reg_email(text=valid_reg_email)
        page.enter_reg_password(text=empty_password)
        page.click_checkbox()
        page.click_creating_account_btn()
        assert page.get_auth_page() == 'https://excursium.com/Client/Login'