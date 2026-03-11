from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self._url = url
        self._driver = driver

    def get_current_url(self):
        return self._driver.current_url

    def get_page(self, url):
        return self._driver.get(url)


class AuthPage(BasePage):
    def __init__(self, driver, url='https://excursium.com/Client/Login'):
        super().__init__(driver, url)
        self.wait = WebDriverWait(driver,20)
        self._configurate()

    def get_auth_page(self):
        return self._url

    def _configurate(self):
        self.get_page(self._url)

    def enter_email(self, text):
        element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.field-input[type='email']")))
        element.send_keys(text)

    def enter_password(self, text):
        element = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        element.send_keys(text)

    def click_login_btn(self):
        element = self.wait.until(EC.element_to_be_clickable((By.ID, "login-btn")))
        element.click()

    def click_forgot_password_btn(self):
        element = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Забыли пароль?")))
        element.click()

    def is_recovery_mode_active(self):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Отправить код')]"))
            )
            return element.is_displayed()
        except:
            return False

    def click_registration_btn(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Регистрация')]")))
        element.click()

    def enter_reg_email(self, text):
        element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='вы@школа.рф']")))
        element.click()
        element.clear()
        element.send_keys(text)

    def enter_reg_password(self, text):
        element = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Минимум 6 символов']")))
        element.click()
        element.clear()
        element.send_keys(text)

    def click_checkbox(self):
        element = self.wait.until(EC.presence_of_element_located((By.ID, "isAgreement")))
        self._driver.execute_script("arguments[0].click();", element)

    def click_creating_account_btn(self):
        element = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(), 'Создать аккаунт')]")))
        element.click()

    def is_confirm_visible(self, timeout=10):
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(), 'Подтвердить')]")))
            return True
        except:
            return False

    def is_registration_tab_active(self):
        btn = self._driver.find_element(By.XPATH, "//button[text()='Регистрация']")
        return "active" in btn.get_attribute("class")

    def click_privacy_policy_btn(self):
        element = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "политику конфиденциальности")))
        element.click()

    def click_user_agreementy_btn(self):
        element = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "пользовательское соглашение")))
        element.click()
