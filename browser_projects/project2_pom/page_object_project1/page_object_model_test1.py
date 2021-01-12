#Step 1
#This is the most basic use of page objects broken into separate modules

from selenium import webdriver

from training_ground_page import TrainingGroundPage
from trial_of_stones_page import TrialPage

# Test Setup - Training Ground 
browser = webdriver.Chrome()
test_value = 'it worked'

# Test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1'

browser.quit()