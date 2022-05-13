import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from hamcrest import assert_that, is_


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def click(self, locator):
        self.wait_for(EC.element_to_be_clickable(locator)).click()


    def find(self, locator):
        element = self.wait_for(EC.visibility_of_element_located(locator))
        return element


    def elements_by_id(self, id):
        return self.driver.find_elements_by_id(id)


    def elements_by_class(self, class_name):
        return self.driver.find_elements_by_class_name(class_name)


    def elements_by_xpath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)


    def find_element(self, element):
        return self.driver.find_element(*element)


    def wait_for(self, condition, seconds = 10):
        return WebDriverWait(self.driver, seconds).until(condition)


    def type_in(self, locator, text, set_clear = True):
        element = self.find(locator)
        if set_clear:
            element.clear()
        element.set_value(text)


    def get_text_element(self,locator):
        return self.find(locator).text


    def custom_wait_implicit(self, element):
        i = 0
        state = False
        # verificando se existem elementos com o identificador 'element' enviado
        elementoExiste = len(self.driver.find_elements(*element))
        # loop que valida timeout (time * 0.5 = 20sgs) ou se elemento existe, sai do loop
        while(i<=40):
            elementoExiste = len(self.driver.find_elements(*element))
            time.sleep(0.5)
            if(elementoExiste > 0):
                state = True
                break
            i+=1
        if state == False:
            print("Elemento "+str(element)+ " não encontrado")


    def wait_unit(self, condition, seconds):
        return WebDriverWait(self.driver, seconds).until(condition)


    def find_element_visibility(self, locator):
        element = self.wait_unit(EC.visibility_of_element_located(locator), 60)
        return element


    def validar_text_elemento(self, elementoText, msgText):
        assert_that(self.get_text_element(elementoText
            ), is_(msgText))