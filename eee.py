from selenium.common.exceptions import NoSuchElementException

try:
    if (5 == 6):
        print(4)
except NoSuchElementException as e:
    print(e)
