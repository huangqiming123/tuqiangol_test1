from selenium import webdriver

driver = webdriver.PhantomJS()

driver.get('http://www.baidu.com')

driver.save_screenshot('aaa.png')
