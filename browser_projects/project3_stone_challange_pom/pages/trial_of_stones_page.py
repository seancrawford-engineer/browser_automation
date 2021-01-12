from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class TrialPage(BasePage):
    
    url = 'https://techstepacademy.com/trial-of-the-stones'
    
    @property
    def stone_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r1Input')
        return BaseElement(driver=self.driver, locator=locator)
    
    @property
    def stone_button(self):
        locator = Locator = (By.CSS_SELECTOR, 'button#r1Btn')
        return BaseElement(driver=self.driver, locator=locator)
    
    @property
    def get_stone_ans(self):
        locator = Locator(By.CSS_SELECTOR, 'div#passwordBanner > h4')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def secrets_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r2Input')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def secrets_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r2Butn')
        return BaseElement(driver=self.driver, locator=locator)
    
    @property
    def get_merchant(self):
        locator = Locator(By.XPATH, "//p[text()='3000']/../span/b")
        return BaseElement(driver=self.driver, locator=locator)
    
    @property
    def merchant_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r3Input')
        return BaseElement(driver=self.driver, locator=locator)
    
    @property
    def merchant_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r3Butn')
        return BaseElement(driver=self.driver, locator=locator)
    
    @property
    def check_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#checkButn')
        return BaseElement(driver=self.driver, locator=locator)
    
    @property
    def complete_banner(self):
        locator = Locator(By.CSS_SELECTOR, 'div#trialCompleteBanner h4')
        return BaseElement(driver=self.driver, locator=locator)

