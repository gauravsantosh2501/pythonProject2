#open the url - https://katalon-demo-cura.herokuapp.com/
#click on the make appoinment button
#verify that url changes - assert
#time.sleep(3)
#enter the username, password
#next page verify the current url
#make appoinment text on the web page

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
from allure_commons.type import AttachmentType

@allure.title("Cura")
@allure.description("Make Appointment")
def test_mini_project():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    make_element = driver.find_element(By.ID,"btn-make-appointment")
    make_element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep()
    user_element = driver.find_element(By.ID,"txt-username")
    user_element.send_keys("John Doe")
    user_element = driver.find_element(By.ID,value="txt-password")
    user_element.send_keys("ThisIsNotAPassword")
    log_in = driver.find_element(By.ID,"btn-login")
    log_in = click()
    time.sleep(3)
    verify_text = driver.find_element(By.XPATH, "//div/h2")
    print(verify_text)  
    assert verify_text.text == "Make Appointment"
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)




