import os
import threading
from time import sleep

import datetime

'''
testcases运行入口
author:zhangAo
'''


def run_test():
    os.system('python -m test_runner.tuqiangOL_test_runner_login')
    sleep(10)
    os.system('python -m test_runner.tuqiangOL_test_runner_account_center')
    sleep(10)
    os.system('python -m test_runner.tuqiangOL_test_runner_global_search')
    sleep(10)
    os.system('python -m test_runner.tuqiangOL_test_runner_cust_manage')
    sleep(10)
    os.system('python -m test_runner.tuqiangOL_test_runner_dev_manage')
    sleep(10)
    os.system('python -m test_runner.tuqiangOL_test_runner_console')
    sleep(10)
    os.system('python -m test_runner.tuqiangOL_test_runner_set_up')
    sleep(10)
    os.system('python -m test_runner.tuqiangOL_test_runner_command_management')
    sleep(10)
    os.system('python -m test_runner.tuqiangOL_test_runner_alarm_info')
    sleep(10)
    os.system('python -m test_runner.tuqiangOL_test_runner_statistical_form')


if __name__ == "__main__":
    start_time = datetime.datetime(2017, 4, 6, 20, 15, 0)
    while datetime.datetime.now() < start_time:
        sleep(5)

    '''thread_list = []
    for i in range(5):
        t1=threading.Thread(target=run_test)
        t1.setDaemon(True)
        thread_list.append(t1)
        t1.start()
        t1.join()'''

    run_test()

    sleep(10)
    os.system('shutdown -s -f')
