from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://114.55.101.5')


# 参数数字为像素点
print("设置浏览器宽480、高800显示")
driver.set_window_size(480, 800)


element = driver.find_element_by_xpath('//*[@id="main"]/article[1]/div/div[2]/header/h2/a')


element.click()


