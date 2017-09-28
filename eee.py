import os
from time import sleep
from tkinter import *

import datetime

master = Tk()
master.geometry('500x300+500+200')
master.title('自动化执行程序')
master.resizable(False, False)


def begin_test():
    y = int(e1.get())
    m = int(e2.get())
    d = int(e3.get())
    h = int(e4.get())
    min = int(e5.get())
    s = int(e6.get())
    print(y, m, d, h, min, s)
    start_time = datetime.datetime(y, m, d, h, min, s)
    while datetime.datetime.now() < start_time:
        sleep(5)
    os.system('python -m testcases.dev_manage.test_case_71_dev_manage_dev_search_by_imei')


# 第一行抬头
l1 = Label(master, text='请输入开始运行的时间：').grid(row=0)
# 第二行输入年月日
t1 = StringVar()
t1.set('2017')
e1 = Entry(master, width=10, textvariable=t1)
e1.grid(row=2, column=0)
l2 = Label(master, text='年').grid(row=2, column=1)

e2 = Entry(master, width=10)
e2.grid(row=3, column=0)
l3 = Label(master, text='月').grid(row=3, column=1)

e3 = Entry(master, width=10)
e3.grid(row=4, column=0)
l4 = Label(master, text='日').grid(row=4, column=1)

e4 = Entry(master, width=10)
e4.grid(row=5, column=0)
l5 = Label(master, text='时').grid(row=5, column=1)

e5 = Entry(master, width=10)
e5.grid(row=6, column=0)
l6 = Label(master, text='分').grid(row=6, column=1)

t2 = StringVar()
t2.set('0')
e6 = Entry(master, width=10, textvariable=t2)
e6.grid(row=7, column=0)
l7 = Label(master, text='秒').grid(row=7, column=1)

var = IntVar()


def test_and_on_line():
    if var.get() == 1:
        return '测试'
    elif var.get() == 2:
        return '线上'


r1 = Radiobutton(master, text="测试", variable=var, value=1, command=test_and_on_line)
r1.grid(row=8, column=0)

r2 = Radiobutton(master, text="线上", variable=var, value=2, command=test_and_on_line)
r2.grid(row=8, column=1)
Button(master, text='开始执行', command=begin_test, width=10, height=1).grid(row=9, column=0)
Button(master, text='退出', command=quit, width=10, height=1).grid(row=9, column=1)

mainloop()
