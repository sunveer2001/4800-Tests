from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Create a new WebDriver instance
driver = webdriver.Chrome() 
# chrome_options = Options()
# driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe", options=chrome_options )

# Logs into website
def LOGIN_TEST():
   try:
      driver.get('http://ec2-54-151-18-23.us-west-1.compute.amazonaws.com/login')
      driver.implicitly_wait(5)
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
   try:
      driver.implicitly_wait(5)
      element = driver.find_element(by=By.ID, value='contcont')
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
      text_box = driver.find_element(by=By.CLASS, value='form-control')
      text_box.send_keys("Test")
      text_box.send_keys(Keys.RETURN)
      assert driver.current_url == output_page
   except Exception as e:
      return False
   return True

# Input validation is present and functional
def INPUT_VALID_TEST():
   input_file = "./text/input_valid.txt"
   text_box = driver.find_element(by=By.CLASS, value='form-control')
   try:
      with open(input_file, 'r') as file:
         for line_number, line in enumerate(file, start=1):
            #print(f"Processing line {line_number}: {line.strip()}")
            driver.implicitly_wait(5)
            text_box.send_keys(line)
            assert text_box.send_keys(Keys.RETURN)
   except Exception as e:
      return False
   return True
         
# Output displays properly
def OUTPUT_TEST():
   input_file = "./text/input_output.txt"
   text_box = driver.find_element(by=By.CLASS, value='form-control')
   output = driver.find_element(by=By.CLASS, value='alert alert-sucess')
   try:
      with open(input_file, 'r') as file:
         for line_number, line in enumerate(file, start=1):
            #print(f"Processing line {line_number}: {line.strip()}")
            line = line.split(" | ")
            driver.implicitly_wait(5)
            text_box.send_keys(line[0])
            text_box.send_keys(Keys.RETURN)
            assert output.text == line[1]
   except Exception as e:
      return False
   return True

print(LOGIN_TEST())
#print(UI_TEST())
print(BUTTON_TEST())
print(INPUT_VALID_TEST())

time.sleep(5)
# Close the browser
driver.quit()