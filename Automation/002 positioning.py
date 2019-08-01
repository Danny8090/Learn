from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://114.55.101.5') 

element = driver.find_element_by_xpath('//*[@id="main"]/article[1]/div/div[2]/header/h2/a')

element.click()

driver.quit()