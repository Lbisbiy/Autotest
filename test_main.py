# -*- coding: utf-8 -*-
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pageObject.Data import Data
from pageObject.LoginPage import LoginPage
from pageObject.ParserPage import ParserPage
from pageObject.SendingPage import SendingPage


class TestMailSearch:

    def setup(self):
        self.chrome = "chromedriver.exe"
        self.driver = webdriver.Chrome(self.chrome)
        self.wait = WebDriverWait(self.driver, 500)
        self.driver.get('https://www.google.com/intl/ru/gmail/about/#')

    @allure.feature('Отправка письма')
    @allure.story('Тест')
    def test_login(self):
        data = Data()
        with allure.step('Заходим на почту'):
            driver = LoginPage().sig_in_page(self.driver, data)
        assert driver.title == 'Gmail'
        with allure.step('Парсим'):
            letter = ParserPage().parser_letters(driver, data.checkAddress).__str__()
        SendingPage().send_letter(driver, data, letter)

    def teardown(self):
        self.driver.close()


if __name__ == '__main__':
    pytest.main()
