from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.techstepacademy.com/trial-of-the-stones")

#Riddle Of Stones
input1_elem = browser.find_element_by_css_selector("input[id='r1Input']")
input1_elem.send_keys("rock")
button1_elem = browser.find_element_by_css_selector("button[id='r1Btn']")
button1_elem.click()
stone_riddle_ans = browser.find_element_by_css_selector("div#passwordBanner > h4")
text_of_stone_ans = stone_riddle_ans.text

#Riddle Of Secrets
input2_elem = browser.find_element_by_css_selector("input[id='r2Input']")
input2_elem.send_keys(text_of_stone_ans)
button2_elem = browser.find_element_by_css_selector("button[id='r2Butn']")
button2_elem.click()

#The Two Merchants
merchant1_elem = browser.find_element_by_xpath("//p[text()='3000']/../span/b")
merchant_name = merchant1_elem.text
input3_elem = browser.find_element_by_css_selector("input[id='r3Input']")
input3_elem.send_keys(merchant_name)
button3_elem = browser.find_element_by_css_selector("button#r3Butn")
button3_elem.click()
button4_elem = browser.find_element_by_css_selector("button#checkButn")
button4_elem.click()
completion_msg_elem = browser.find_element_by_css_selector("div#trialCompleteBanner h4")
completion_msg = completion_msg_elem.text

assert completion_msg == "Trial Complete"


