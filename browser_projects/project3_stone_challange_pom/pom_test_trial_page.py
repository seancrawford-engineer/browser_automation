from selenium import webdriver

from pages.trial_of_stones_page import TrialPage

# Test Setup
browser = webdriver.Chrome()
test_value = 'rock'

# Test
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.input_text(test_value)
trial_page.stone_button.click()
trial_page.secrets_input.input_text(trial_page.get_stone_ans.text)
trial_page.secrets_button.click()
trial_page.merchant_input.input_text(trial_page.get_merchant.text)
trial_page.merchant_button.click()
trial_page.check_button.click()
completion_msg = trial_page.complete_banner.text
assert completion_msg == "Trial Complete", f"Completion Banner ({complete_banner.text}) does not match expected Tial Complete"
print("Test Passed")
browser.quit()