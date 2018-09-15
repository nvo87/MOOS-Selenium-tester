from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import signal
import time


class SeleniumTestWrapper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        # Take and run chromedriver from script folder
        dir_path = os.path.dirname(os.path.realpath(__file__))
        chromedriver = dir_path + '/chromedriver'
        os.environ['webdriver.chrome.driver'] = chromedriver
        self.driver = webdriver.Chrome(
            chrome_options=options, executable_path=chromedriver)

    # hold the pause, in sec
    def timer_practice(self, sec):
        time.sleep(sec)

    def goto_site(self, site='https://www.yandex.ru/'):
        self.driver.get(site)

    def wait_element(self, selector, name):
        try:
            ui.WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((selector, name)))
        except TimeoutException as e:
            print('There is no such element - ' + name, e)
            self.tear_down()

    def click_element(self, selector, name):
        self.wait_element(selector, name)
        self.driver.find_element(selector, name).click()

    def select_option(self, selector, name, option_text):
        self.wait_element(selector, name)
        select = ui.Select(self.driver.find_element(selector, name))
        select.select_by_value(option_text)

    def input_text(self, selector, name, text):
        self.wait_element(selector, name)
        element = self.driver.find_element(selector, name)
        element.send_keys(text)

    def tear_down(self):
        pid = self.driver.service.process.pid
        self.driver.close()
        # self.driver.quit()
        try:
            os.kill(int(pid), signal.SIGTERM)
            print("Killed chrome using process")
        except ProcessLookupError as ex:
            pass