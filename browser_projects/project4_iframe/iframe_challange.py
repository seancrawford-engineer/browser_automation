from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.get("https://www.techstepacademy.com/iframe-training")
browser.execute_script('window.open("https://www.techstepacademy.com/iframe-training", "_blank");')

handles = browser.window_handles
handle_size = len(browser.window_handles)
browser.switch_to.window(handles[0])

for handle in range(handle_size):
    browser.switch_to.window(handles[handle])
    iframe = browser.find_element_by_css_selector("iframe")
    browser.switch_to.frame(iframe)
    
    welcome_text = browser.find_element_by_css_selector("div#block-ec928cee802cf918d26c div p").text
    input()
    button1 = browser.find_element_by_css_selector("button#b1")
    button1.click()
    input()
    WebDriverWait(browser, 10).until(alert_is_present())
    alert = Alert(browser)
    alert_text = alert.text
    alert.accept()
    input()
    sel = browser.find_element_by_id('sel1')
    my_select = Select(sel)
    my_select.select_by_index(0)
    select_text = my_select.first_selected_option.text
    input()
    browser.switch_to.default_content()
    title_text = browser.find_element_by_css_selector("div#block-5d3de848045889000188d389 div p").text

    print(title_text)
    print(welcome_text)
    print(alert_text)
    print(select_text)

browser.quit()
