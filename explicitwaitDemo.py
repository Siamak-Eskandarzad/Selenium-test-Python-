import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
list = []
list2 = []
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("b")
time.sleep(2)
carts = driver.find_elements(By.XPATH,"//div[@class='product-action']")
count = len(carts)
print(count)
for cart in carts:
    list.append(cart.find_element(By.XPATH, "parent::div/h4").text)
    cart.click()
print(list)
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[class='promoCode']")))
vegits=driver.find_elements(By.CSS_SELECTOR,"p[class='product-name']")
for veg in vegits:
    list2.append(veg.text)
print(list2)
assert list == list2
driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,"button[class='promoBtn']").click()
wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
print(driver.find_element(By.XPATH,"//span[@class='promoInfo']").text)


