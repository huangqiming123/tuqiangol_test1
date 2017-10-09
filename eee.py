'''import os
import os.path
import datetime

base_dir = "E:\\git\\jimi10086_test\\data\\"
l = os.listdir(base_dir)
l.sort(key=lambda fn: os.path.getmtime(base_dir + fn) if not os.path.isdir(base_dir + fn) else 0)
d = datetime.datetime.fromtimestamp(os.path.getmtime(base_dir + l[-1]))
# print('最后改动的文件是' + l[-1] + ",时间:" + d.strftime("%Y年%m月%d日 %H时%M分%S秒"))
print(l[-1])


def move(n, a, b, c):
    if n == 1:
        print('%s --> %s' % (a, c))
    else:
        move((n - 1), a, c, b)
        move(1, a, b, c)
        move((n - 1), b, a, c)


move(2, 'A', 'B', 'C')'''

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
var2 = IntVar()


def test_and_on_line():
    if var.get() == 1:
        return '测试'
    elif var.get() == 2:
        return '线上'


l8 = Label(master, text='运行环境：').grid(row=8, column=0, sticky=W)

r1 = Radiobutton(master, text="测试", variable=var, value=1, command=test_and_on_line)
r1.grid(row=9, column=0)

r2 = Radiobutton(master, text="线上", variable=var, value=2, command=test_and_on_line)
r2.grid(row=9, column=1)

l9 = Label(master, text='是否运行后关机：').grid(row=10, column=0, sticky=W)

r1 = Radiobutton(master, text="是", variable=var2, value=3, command=test_and_on_line)
r1.grid(row=11, column=0)

r2 = Radiobutton(master, text="否", variable=var2, value=4, command=test_and_on_line)
r2.grid(row=11, column=1)

Button(master, text='开始执行', command=begin_test, width=10, height=1).grid(row=12, column=0)
Button(master, text='退出', command=quit, width=10, height=1).grid(row=12, column=1)

mainloop()
