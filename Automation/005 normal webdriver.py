from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("python")
time.sleep(2)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
driver.back()
search_text = driver.find_element_by_id("kw")
search_text.send_keys('Java')
search_text.submit()


driver.get("https://www.baidu.com")


#获取输入框的尺寸
size = driver.find_element_by_id("kw").size
print(size)

#返回百度页面底部备案信息
text = driver.find_element_by_id("cp").text
print(text)

#返回原元素属性值。可以是id、name、type或其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type') 
print(attribute)


#返回元素结果是否可见，返回结果为True或者False
result = driver.find_element_by_id("kw").is_displayed()
print(result)


driver.quit()

