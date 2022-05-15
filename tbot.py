#tinder bot for fb login,

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.action_chains import ActionChains


username = 'USERNAME'
password = 'PASSWORD'

driver = webdriver.Chrome() #open chrome
driver.get('https://www.tinder.com')  #go to tinder
time.sleep(0.5) #allow page to load


main_page_handle = driver.current_window_handle

#click login
driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
time.sleep(0.5)
#click fb login
driver.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()


time.sleep(1)
#switch to fb login popup
login_popup = None
for handle in driver.window_handles:
    if handle != main_page_handle:
        login_popup = handle
        break
driver.switch_to.window(login_popup)

#input username and password
driver.find_element(by = By.XPATH, value = '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input').send_keys(username)
driver.find_element(by = By.XPATH, value = '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input').send_keys(password)
#click login
driver.find_element(by = By.XPATH, value = '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input').click() 


#switch back to main page
driver.switch_to.window(main_page_handle)

time.sleep(5)
#click decline and allow location
driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button').click() #cookies
driver.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div/div/div/div[3]/button[1]').click() #allow location
driver.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div/div/div/div[3]/button[2]').click() #notifications

time.sleep(5)

while True:
    time.sleep(0.1)

    try:
        driver.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div/div[3]/button[2]').click()
        break
    except:
        person_img = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[1]/div[1]')
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(person_img, 200, 0).perform()
