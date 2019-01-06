# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SendingPage:
    def __init__(self):
        self._buttonCreateLetter = "//div[@class='T-I J-J5-Ji T-I-KE L3']"
        self._addressForm = "//textarea[@aria-label='Кому']"
        self._topicLetterForm = "//input[@name='subjectbox']"
        self._textLetterForm = "//div[@aria-label='Тело письма']"
        self._buttonSend = "//div[@class='T-I J-J5-Ji aoO T-I-atl L3']"
        self._confirmationForm = "//span[.='Письмо отправлено.']"

    def send_letter(self, driver, data, letter):
        wait = WebDriverWait(driver, 500)
        writer = driver.find_element_by_xpath(self._buttonCreateLetter)
        writer.click()
        with allure.step('Отправка письма'):
            wait.until(EC.visibility_of_element_located((By.XPATH, self._addressForm)))
            address = driver.find_element_by_xpath(self._addressForm)
            address.send_keys(data.checkAddress)
            topic = driver.find_element_by_xpath(self._topicLetterForm)
            topic.send_keys(data.topicForLetter)
            text = driver.find_element_by_xpath(self._textLetterForm)
            text.send_keys(letter)
            driver.find_element_by_xpath(self._buttonSend).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,  self._confirmationForm)))


