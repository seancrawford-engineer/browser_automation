from selenium import webdriver

from trial_of_stones_page import TrialPage

# Test Setup
browser = webdriver.Chrome()
test_value = 'rock'

# Test
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.input_text(test_value)
assert trial_page.stone_button.text == 'Answer', "Unexpected button1 text"
trial_page.stone_button.click()
browser.quit()