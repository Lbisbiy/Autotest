# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ParserPage:
    def __init__(self):
        self._buttonAdvancedSearch = "//button[@aria-label='Расширенный поиск']"
        self._addressForm = "//div[@style='visibility: visible; top: 56px;']//input[@class='ZH nr aQa']"
        self._listLetters = "//div[@class='ae4 UI UJ']//tr[@class='zA yO']"

    def parser_letters(self, driver, check_address):
        wait = WebDriverWait(driver, 500)
        wait.until(EC.visibility_of_element_located((By.XPATH, self._buttonAdvancedSearch)))
        driver.find_element_by_xpath(self._buttonAdvancedSearch).click()
        with allure.step('Фильтруем письма'):
            wait.until(EC.visibility_of_element_located((By.XPATH, self._addressForm)))
            address = driver.find_element_by_xpath(self._addressForm)
            address.send_keys(check_address)
            address.send_keys(Keys.ENTER)
            wait.until(EC.visibility_of_element_located((By.XPATH, self._listLetters)))
            table = driver.find_elements_by_xpath(self._listLetters)
        with allure.step('считаем количество писем'):
            quantity = len(table)
        return quantity

