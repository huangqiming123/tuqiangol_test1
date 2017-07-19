import os
import threading
from time import sleep
import datetime

'''
testcases运行入口
author:zhangAo
'''


def run_01():
    '''os.system('python -m test_runner.tuqiangOL_test_runner_login')
    sleep(5)
    os.system('python -m test_runner.tuqiangOL_test_runner_account_center')'''
    os.system('python -m test_runner.tuqiangOL_test_runner_dev_manage')
    sleep(5)


def run_02():
    os.system('python -m test_runner.tuqiangOL_test_runner_global_search')
    sleep(5)


def run_03():
    # os.system('python -m test_runner.tuqiangOL_test_runner_cust_manage')
    os.system('python -m test_runner.tuqiangOL_test_runner_command_management')
    sleep(5)
    os.system('python -m test_runner.tuqiangOL_test_runner_safe_area')


def run_04():
    os.system('python -m test_runner.tuqiangOL_test_runner_statistical_form')


'''def run_05():
    os.system('python -m test_runner.tuqiangOL_test_runner_account_center')


def run_06():
    os.system('python -m test_runner.tuqiangOL_test_runner_command_management')
    sleep(5)


def run_07():
    os.system('python -m test_runner.tuqiangOL_test_runner_safe_area')
    sleep(5)


def run_08():
    os.system('python -m test_runner.tuqiangOL_test_runner_statistical_form')'''


def run_09():
    os.system('python -m test_runner.tuqiangOL_test_runner_account_log')
    sleep(10)


'''while 1:
    print('请输入开始运行时间')
    print('月、日、小时、分钟 用“/”隔开(如：5/26/17/15)')
    print('如现在运行，请输入now')
    time = input('请输入：')
    if time == 'now':
        break
    try:
        month = time.split('/')[0]
        day = time.split('/')[1]
        hour = time.split('/')[2]
        min = time.split('/')[3]
        if month.isdigit() and day.isdigit() and hour.isdigit() and min.isdigit():
            if month <= 12 and day <= 31 and hour <= 23 and min <= 59:
                start_time = datetime.datetime(2017, int(month), int(day), int(hour), int(min), 0)
                while datetime.datetime.now() < start_time:
                    sleep(5)
                break
            else:
                print('输入有误，请重新输入！')
                continue
        else:
            print('输入有误，请重新输入！')
            continue
    except:
        print('输入有误，请重新输入！')
        continue'''
start_time = datetime.datetime(2017, 7, 19, 1, 10, 0)
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

'''for i5 in range(1):
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

for i8 in range(1):
    t8 = threading.Thread(target=run_08)
    t8.setDaemon(True)
    thread_list.append(t8)'''

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()

run_09()
# 运行后自动关机
sleep(10)
os.system('shutdown -s -f')
