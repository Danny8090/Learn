from selenium import webdriver

#引入keys模块
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")

#删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)