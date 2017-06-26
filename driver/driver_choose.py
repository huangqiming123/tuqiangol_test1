from selenium import webdriver


# 指定浏览器驱动
def browser(browser_name):
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
        return driver
    elif browser_name == 'ie':
        driver = webdriver.Ie()
        return driver
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
        return driver
