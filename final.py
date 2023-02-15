# Automation
# https://testautomationpractice.blogspot.com/


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

ser_obj = Service()
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()
time.sleep(2)

# Searchbar
searchbar = driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']")
searchbar.send_keys("Stranger Things")
driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//input[@type='submit']").click()

# Alert
time.sleep(3)
driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
time.sleep(3)
driver.switch_to.alert.accept()

# Date Picker
time.sleep(3)
datepicker = driver.find_element(By.XPATH,"//*[@id='datepicker']")
datepicker.send_keys("08/25/2022")

# Select menu
time.sleep(2)
speed = Select(driver.find_element(By.XPATH,"//select[@id='speed']"))
speed.select_by_visible_text("Medium")

time.sleep(2)
files = Select(driver.find_element(By.XPATH,"//select[@id='files']"))
files.select_by_index("2")

time.sleep(2)
num = Select(driver.find_element(By.XPATH,"//select[@id='number']"))
num.select_by_index("2")

time.sleep(2)
product = Select(driver.find_element(By.XPATH,"//select[@id='products']"))
product.select_by_visible_text("Bing")

time.sleep(2)
animal = Select(driver.find_element(By.XPATH,"//select[@id='animals']"))
animal.select_by_value("avatar")

# Text Labels
# Print in terminal
print();print()
label1 = driver.find_element(By.XPATH,"//*[@id='Text1']/div[1]/span")
print(label1.text)
label2 = driver.find_element(By.XPATH,"//*[@id='Text1']/div[1]/div[1]/span")
print(label2.text)
label3 = driver.find_element(By.XPATH,"//*[@id='Text1']/div[1]/div[2]/span")
print(label3.text)
label4 = driver.find_element(By.XPATH,"//*[@id='Text1']/div[1]/div[3]/span")
print(label4.text)
label5 = driver.find_element(By.XPATH,"//*[@id='Text1']/div[1]/div[4]/span")
print(label5.text)
label6 = driver.find_element(By.XPATH,"//*[@id='Text1']/div[1]/div[5]/span")
print(label6.text)
print();print()

time.sleep(2)

# Xpath Axes
# Print in terminal
emp = driver.find_elements(By.XPATH,"//*[@id='HTML14']/div[1]/empinfo")
for x in emp:
    print(x.text)

print();print()
time.sleep(2)

# Form
driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="frame-one1434677811"]'))
driver.find_element(By.XPATH,"//*[@id='RESULT_TextField-1']").send_keys("Ujang")
driver.find_element(By.XPATH,"//*[@id='RESULT_TextField-2']").send_keys("Bahari")
driver.find_element(By.XPATH,"//*[@id='RESULT_TextField-3']").send_keys("+62897xxxxxxx")
driver.find_element(By.XPATH,"//*[@id='RESULT_TextField-4']").send_keys("Indonesia")
driver.find_element(By.XPATH,"//*[@id='RESULT_TextField-5']").send_keys("DKI Jakarta")
driver.find_element(By.XPATH,"//*[@id='RESULT_TextField-6']").send_keys("ujangbahari@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//label[@for='RESULT_RadioButton-7_0']").click()

# Checkbox

time.sleep(2)
driver.find_element(By.XPATH,"//label[@for='RESULT_CheckBox-8_1']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//label[@for='RESULT_CheckBox-8_2']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//label[@for='RESULT_CheckBox-8_3']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//label[@for='RESULT_CheckBox-8_4']").click()

# Radio Button
time.sleep(2)
radio = Select(driver.find_element(By.XPATH,"//*[@id='RESULT_RadioButton-9']"))
radio.select_by_visible_text("Afternoon")

# Upload File
# The files must be in systems
time.sleep(3)
files = driver.find_element(By.ID,"RESULT_FileUpload-10").send_keys("D:/A-Test/0.py")

time.sleep(2)
# Leaving Frame
driver.switch_to.default_content()
time.sleep(2)

# Double Click
ele = driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
action = ActionChains(driver)
action.double_click(ele).perform()

# Drag and Drop
time.sleep(2)
element = driver.find_element(By.XPATH,'//*[@id="draggable"]')
square = driver.find_element(By.XPATH,'//*[@id="droppable"]')

action = ActionChains(driver)
action.drag_and_drop(element, square).perform()

# Drag and Drop Images
time.sleep(2)
photo1 = driver.find_element(By.XPATH,'//*[@id="gallery"]/li[1]')
time.sleep(3)
photo2 = driver.find_element(By.XPATH,'//*[@id="gallery"]/li[2]')
trash = driver.find_element(By.XPATH,'//*[@id="trash"]')

action = ActionChains(driver)
action.drag_and_drop(photo1, trash).perform()
time.sleep(2)
action2 = ActionChains(driver)
action2.drag_and_drop(photo2, trash).perform()

# Slider
time.sleep(2)
slider = driver.find_element(By.XPATH,'//*[@id="slider"]/span')
action = ActionChains(driver)
action.drag_and_drop_by_offset(slider, 200, 0).perform()
time.sleep(3)

# Resize
resize = driver.find_element(By.XPATH,"//div[@id='resizable']")
dragging = driver.find_element(By.XPATH,"//*[@id='resizable']/div[3]")
action = ActionChains(driver)
action.click_and_hold(dragging)
action.drag_and_drop_by_offset(dragging, 200, 0).perform()
time.sleep(3)
action.drag_and_drop_by_offset(dragging, 0, 100).perform()

time.sleep(3)
driver.close()