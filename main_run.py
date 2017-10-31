import os
import threading
from time import sleep
import datetime


def run_01():
    os.system('python -m test_runner.tuqiangOL_test_runner_account_center')
    sleep(5)
    os.system('python -m test_runner.tuqiangOL_test_runner_account_center2')
    # os.system('python -m test_runner.tuqiangOL_test_runner_login')
    # sleep(5)
    # os.system('python -m test_runner.tuqiangOL_test_runner_account_center')
    # os.system('python -m test_runner.tuqiangOL_test_runner_dev_manage')
    # sleep(5)


def run_02():
    os.system('python -m test_runner.tuqiangOL_test_runner_command_management')
    sleep(5)
    os.system('python -m test_runner.tuqiangOL_test_runner_cust_manage')
    # os.system('python -m test_runner.tuqiangOL_test_runner_global_search')
    # sleep(5)
    # os.system('python -m test_runner.tuqiangOL_test_runner_account_center')


def run_03():
    os.system('python -m test_runner.tuqiangOL_test_runner_dev_manage')
    sleep(5)
    os.system('python -m test_runner.tuqiangOL_test_runner_global_search')
    # os.system('python -m test_runner.tuqiangOL_test_runner_cust_manage')
    # sleep(5)
    # os.system('python -m test_runner.tuqiangOL_test_runner_command_management')
    # os.system('python -m test_runner.tuqiangOL_test_runner_statistical_form2')


def run_04():
    os.system('python -m test_runner.tuqiangOL_test_runner_login')
    sleep(5)
    os.system('python -m test_runner.tuqiangOL_test_runner_safe_area')
    # os.system('python -m test_runner.tuqiangOL_test_runner_command_management')
    # sleep(2)
    # os.system('python -m test_runner.tuqiangOL_test_runner_statistical_form')


def run_05():
    os.system('python -m test_runner.tuqiangOL_test_runner_statistical_form')
    sleep(5)
    os.system('python -m test_runner.tuqiangOL_test_runner_statistical_form2')


def run_06():
    os.system('python -m test_runner.tuqiangOL_test_runner_statistical_form3')
    sleep(5)


'''def run_07():
    os.system('python -m test_runner.tuqiangOL_test_runner_safe_area')
    sleep(5)


def run_08():
    os.system('python -m test_runner.tuqiangOL_test_runner_statistical_form')'''


def run_09():
    os.system('python -m test_runner.tuqiangOL_test_runner_account_log')
    sleep(10)


start_time = datetime.datetime(2017, 10, 31, 1, 10, 0)
while datetime.datetime.now() < start_time:
    sleep(5)

# 设置线程
thread_list = []
for i in range(1):
    t1 = threading.Thread(target=run_01)
    t1.setDaemon(True)
    thread_list.append(t1)

for i1 in range(1):
    t2 = threading.Thread(target=run_02)
    t2.setDaemon(True)
    thread_list.append(t2)

for i3 in range(1):
    t3 = threading.Thread(target=run_03)
    t3.setDaemon(True)
    thread_list.append(t3)

for i4 in range(1):
    t4 = threading.Thread(target=run_04)
    t4.setDaemon(True)
    thread_list.append(t4)

for i5 in range(1):
    t5 = threading.Thread(target=run_05)
    t5.setDaemon(True)
    thread_list.append(t5)

for i6 in range(1):
    t6 = threading.Thread(target=run_06)
    t6.setDaemon(True)
    thread_list.append(t6)

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()

run_09()
# 运行后自动关机
sleep(10)
os.system('shutdown -s -f')
