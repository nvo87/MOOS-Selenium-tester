from selenium_wrapper import SeleniumTestWrapper
from selenium_wrapper import By
from pandas import ExcelFile


class Test:
    """
    Usefull methods for any test cases
    """
    def __init__(self):
        self.obj = SeleniumTestWrapper()

    def go_to_page(self, site='http://ya.ru'):
        self.obj.goto_site(site)

    def get_dict_from_xls(self, filename):
        xls = ExcelFile(filename)
        df = xls.parse(xls.sheet_names[0])
        return df.to_dict(orient='records')

    def finish_test(self):
        ''' Sleep some time and close webdriver process '''
        obj.timer_practice(5)
        obj.tear_down()


class CamundaTest(Test):
    """
    Specific camunda testing methods
    """
    def login_camunda(self, login, password):
        self.obj.input_text(By.CSS_SELECTOR, 'input[ng-model="username"]', login)
        self.obj.input_text(By.CSS_SELECTOR, 'input[ng-model="password"]', password)
        self.obj.click_element(By.CSS_SELECTOR, 'button[type="submit"]')
        self.obj.click_element(By.CSS_SELECTOR, '.tasklist-app a.ng-binding')

    def go_into_process(self, link_text):
        self.obj.click_element(By.CSS_SELECTOR, 'li.start-process-action a.ng-binding')
        self.obj.timer_practice(5)
        self.obj.click_element(By.LINK_TEXT, link_text)

    def fill_process_form(self, form_data: dict):
        i = 0
        for key, value in form_data.items():
            i += 1
            self.obj.click_element(By.CSS_SELECTOR, 'a[ng-click="addVariable()"]')
            self.obj.input_text(By.XPATH, '(//input[@ng-model="variable.name"])[' + str(i) + ']', key)
            self.obj.select_option(By.XPATH, '(//select[@ng-model="variable.type"])[' + str(i) + ']', 'String')
            self.obj.input_text(By.XPATH, '(//input[@ng-model="variable.value"])[' + str(i) + ']', value)
        self.obj.click_element(By.CSS_SELECTOR, 'button[ng-click="startProcessInstance()"')