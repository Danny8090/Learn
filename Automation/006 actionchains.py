from selenium import webdriver

#引入ActionChains类
导入提供鼠标操作的 ActionChains 类。
from selenium.webdriver.common.action_chains import ActionChains

#perform()： 执行所有 ActionChains 中存储的行为；

#context_click()： 右击；

#double_click()： 双击；

#drag_and_drop()： 拖动；

#move_to_element()： 鼠标悬停。

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")


#定位到要悬停的元素

above = driver.find_element_by_link_text("设置")

#对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()


#from selenium.webdriver import ActionChains
#导入提供鼠标操作的 ActionChains 类。

#ActionChains(driver)
#调用 ActionChains()类， 将浏览器驱动 driver 作为参数传入。

#move_to_element(above)
#context_click()方法用于模拟鼠标右键操作， 在调用时需要指定元素定位。

#perform()
#执行所有 ActionChains 中存储的行为， 可以理解成是对整个操作的提交动作。