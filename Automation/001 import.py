from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://114.55.101.5')

print(driver.title)

driver.quit()