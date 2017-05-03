from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase

driver = AutomateDriver()
base_url = driver.base_url
log_in = LogInBase(driver, base_url)
base_page = BasePage(driver, base_url)
base_page.open_page()
sleep(2)
driver.set_window_max()
log_in.log_in_jimitest()
sleep(2)

driver.click_element('x,//*[@id="customerManagement"]/a')
sleep(2)

'''number = len(
    list(driver.get_elements('x,/html/body/div[2]/div[5]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/ul/li/ul/li')))

for n in range(number):
    sleep(2)
    el = driver.get_element(
        'x,/html/body/div[2]/div[5]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/ul/li/ul/li[%s]/span' % str(n + 1))
    a = el.get_attribute('class')
    driver.execute_script(el)
    sleep(2)
    if a == 'button level1 switch noline_close':
        el.click()

        number1 = len(list(driver.get_elements(
            'x,/html/body/div[2]/div[5]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/ul/li/ul/li[%s]/ul/li' % str(n + 1))))
        if number1 != 0:
            for n1 in range(number1):
                sleep(2)
                el1 = driver.get_element(
                    'x,/html/body/div[2]/div[5]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/ul/li/ul/li[%s]/ul/li[%s]/span' % (
                    str(n + 1), str(n1 + 1)))
                a1 = el1.get_attribute('class')
                sleep(2)
                if a1 == 'button level2 switch noline_close':
                    el1.click()'''
for n in range(100):
    el = driver.get_element('x,//*[@id="treeDemo_' + str(n + 2) + '_switch"]')
    sleep(1)
    driver.execute_script(el)
    sleep(1)
    el.click()
    sleep(1)
