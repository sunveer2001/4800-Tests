from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Login functions properly
def LOGIN_TEST():
   try:
      username = driver.find_element(by=By.ID, value='uname')
      password = driver.find_element(by=By.ID, value='pword')
      username.send_keys('test')
      password.send_keys('test')
      password.send_keys(Keys.RETURN)
      assert driver.current_url == "http://ec2-54-151-18-23.us-west-1.compute.amazonaws.com/"
   except Exception as e:
      return False
   return True

# UI displays correctly
def UI_TEST():
   classes  = ["navbar", "input-group", "alert", "card-body", "display-5", "display-3", "nav-item", "form-control", "btn", "col-md-6", "navbar-brand", "collapse"]
   for attribute in classes:
      try:
         element = driver.find_element(by=By.CLASS_NAME, value=attribute)
         driver.implicitly_wait(10)
         assert element.is_displayed() 
      except Exception as e:
         return False
   return True

# Navigation buttons function properly:
def BUTTON_TEST():
   home = 'http://ec2-54-151-18-23.us-west-1.compute.amazonaws.com/'
   account = 'http://ec2-54-151-18-23.us-west-1.compute.amazonaws.com/account'
   logout = 'http://ec2-54-151-18-23.us-west-1.compute.amazonaws.com/login'
   urls = [home, account, logout]
   pages = ["home", "account", "login"]
   
   for url, page in zip(urls, pages):
      try:
         driver.implicitly_wait(5)
         button = driver.find_element(by=By.ID, value=page)
         button.click()
         assert driver.current_url == url
      except Exception as e:
         return False
      return True

# Text box works properly
def TEXTBOX_TEST():
   try:
      text_box = driver.find_element(by=By.CLASS_NAME, value='form-control')
      text_box.send_keys("Test")
      entered_text = text_box.get_attribute("value")
      assert entered_text == "Test"
   except Exception as e:
      return False
   return True

# Input validation is present and functional for text box
def INPUT_VALID_TEST():
   try:
      button = driver.find_element(by=By.ID, value="home")
      button.click()
      text_box = driver.find_element(by=By.CLASS_NAME, value='form-control')
      text_box.send_keys("@$#&%^_|><:*=-""()+")
      text_box.send_keys(Keys.RETURN)
      alert = driver.find_element(by=By.CLASS_NAME, value='alert-success')
      assert alert.is_displayed()
   except Exception as e:
      return False
   return True

# Input validation is present and functional for file input
def FILE_VALID_TEST():
   text_box = driver.find_element(by=By.CLASS_NAME, value='form-control')
   try:
      button = driver.find_element(by=By.ID, value="home")
      button.click()
      text_box.click()
      assert text_box.send_keys(Keys.RETURN)
   except Exception as e:
      return False
   return True
         
# Output displays correctly and properly
def OUTPUT_TEST():
   inputs = [("I am happy!", "Positive"), ("This is dumb.", "Negative")]
   for input, result in inputs:
      try:
         button = driver.find_element(by=By.ID, value="home")
         button.click()
         text_box = driver.find_element(by=By.CLASS_NAME, value='form-control')
         text_box.send_keys(input)
         text_box.send_keys(Keys.RETURN)
         driver.implicitly_wait(300)
         output = driver.find_element(by=By.CLASS_NAME, value='alert-success')
         output = (output.text).split()[-1]
         assert output == result
      except Exception as e:
         print(e)
         return False
   return True

# Confirm functionality at various resolutions
def RESOLUTION_TEST():
   resolutions = [(800, 600), (1024, 768), (1280, 720), (1920, 1080)]
   try:
      for width, height in resolutions:
         driver.set_window_size(width, height)
         assert UI_TEST()
         assert BUTTON_TEST()
         assert TEXTBOX_TEST()
   except Exception as e:
      return False
   return True

# Create a new WebDriver instance
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options) 
driver.get('http://ec2-54-151-18-23.us-west-1.compute.amazonaws.com/login')

# Run the tests
print("Tests for login functionality:\t\t", ("Passed" if LOGIN_TEST() else "Failed"))
print("Tests for correct UI display:\t\t", ("Passed" if UI_TEST() else "Failed"))
print("Tests for button functionality:\t\t", ("Passed" if BUTTON_TEST() else "Failed"))
print("Tests for textbox functionality:\t", ("Passed" if TEXTBOX_TEST() else "Failed"))
print("Tests for text input validation:\t", ("Passed" if INPUT_VALID_TEST() else "Failed"))
#print("Tests for file upload validation:\t", ("Passed" if FILE_VALID_TEST() else "Failed"))
print("Tests for correct output:\t\t", ("Passed" if OUTPUT_TEST() else "Failed"))
print("Tests for various resolutions:\t\t", ("Passed" if RESOLUTION_TEST() else "Failed"))

# Close the browser
driver.quit()