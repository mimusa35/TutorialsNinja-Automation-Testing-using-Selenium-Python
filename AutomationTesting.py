import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver: WebDriver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
time.sleep(2)

#Register
driver.find_element(By.XPATH,"//span[normalize-space()='My Account']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
time.sleep(1)
driver.find_element(By.ID,"input-firstname").send_keys("Mimusa")
time.sleep(1)
driver.find_element(By.ID,"input-lastname").send_keys("Mim")
time.sleep(1)
driver.find_element(By.ID,"input-email").send_keys("mimusamim30@gmail.com")
time.sleep(1)
driver.find_element(By.ID,"input-telephone").send_keys("018159876843")
time.sleep(1)
driver.find_element(By.ID,"input-password").send_keys("Fwf@h9n3hf@Aj")
time.sleep(1)
driver.find_element(By.ID,"input-confirm").send_keys("Fwf@h9n3hf@Aj")
time.sleep(2)
driver.find_element(By.NAME,"newsletter").click()
time.sleep(2)
driver.find_element(By.NAME,"agree").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@value='Continue']").click()

#login
driver.find_element(By.XPATH,"//span[normalize-space()='My Account']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("mimusamim30@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("Fwf@h9n3hf@Aj")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(3)

#search
driver.find_element(By.NAME,"search").send_keys("Mac")
time.sleep(1)
driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
time.sleep(3)

#product display page
driver.find_element(By.XPATH,"//div[@class='caption']//a[contains(text(),'MacBook Pro')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//li[3]//a[1]//img[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/div/button[2]").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/button").click()
time.sleep(1)

#add to cart
driver.find_element(By.ID,"button-cart").click()
time.sleep(2)

#shopping cart
driver.find_element(By.XPATH,"//span[normalize-space()='Shopping Cart']").click()
time.sleep(2)

#checkout
driver.find_element(By.XPATH,"//a[@class='btn btn-primary']").click()
time.sleep(2)

#logout
driver.find_element(By.XPATH,"//span[normalize-space()='My Account']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()

time.sleep(2)
driver.quit()