from selenium import webdriver

from pages.training_ground_page import TrainingGroundPage

# Test Setup
browser = webdriver.Chrome()

# Test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1', "Unexpected button1 text"
browser.quit()