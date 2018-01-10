import os
import threading
from time import sleep
import datetime


def run_01():
    os.system('python -m test_runner.tuqiangOL_test_runner_1_log_in')


def run_02():
    os.system('python -m test_runner.tuqiangOL_test_runner_2_user_center')


def run_03():
    os.system('python -m test_runner.tuqiangOL_test_runner_3_set_up')


def run_04():
    os.system('python -m test_runner.tuqiangOL_test_runner_4_customer_management')


def run_05():
    os.system('python -m test_runner.tuqiangOL_test_runner_5_form_search')


def run_06():
    os.system('python -m test_runner.tuqiangOL_test_runner_6_form_port_search')


def run_07():
    os.system('python -m test_runner.tuqiangOL_test_runner_7_form_export')


start_time = datetime.datetime(2018, 1, 10, 1, 10, 0)
while datetime.datetime.now() < start_time:
    sleep(25)

# 设置线程
'''thread_list = []
for i in range(1):
    t1 = threading.Thread(target=run_01)
    t1.setDaemon(True)
    thread_list.append(t1)

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

for i7 in range(1):
    t7 = threading.Thread(target=run_07)
    t7.setDaemon(True)
    thread_list.append(t7)

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()'''
run_01()
sleep(5)
run_02()
sleep(5)
run_03()
sleep(5)
run_04()
sleep(5)
run_05()
sleep(5)
run_06()
sleep(5)
run_07()
# 运行后自动关机
sleep(10)
os.system('shutdown -s -f')
