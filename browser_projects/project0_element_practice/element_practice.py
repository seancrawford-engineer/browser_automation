from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.techstepacademy.com/training-ground")

input2_css_selector = "input[id='ipt2']"
button4_xpath_locator = "//button[@id='b4']"

input2_elem = browser.find_element_by_css_selector(input2_css_selector)
butn4_elem = browser.find_element_by_xpath(button4_xpath_locator)

input2_elem.send_keys("Test text")
butn4_elem.click()

browser.quit()
