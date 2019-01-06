# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self):
        self._signInButton = 'gmail-nav__nav-link__sign-in'
        self._loginForm = 'identifierId'
        self._loginButtonNext = 'identifierNext'
        self._passwordForm = 'password'
        self._passwordButtonNext = 'passwordNext'

    def sig_in_page(self, driver, data):
        wait = WebDriverWait(driver, 500)
        driver.find_element_by_class_name(self._signInButton).click()
        with allure.step('Вводим логин'):
            input_login = driver.find_element_by_id(self._loginForm)
            input_login.send_keys(data.myLogin)
        driver.find_element_by_id(self._loginButtonNext).click()
        with allure.step('Вводим пароль'):
            wait.until(EC.visibility_of_element_located((By.NAME, self._passwordForm)))
            password = driver.find_element_by_name(self._passwordForm)
            password.send_keys(data.myPassword)
        driver.find_element_by_id(self._passwordButtonNext).click()
        return driver


