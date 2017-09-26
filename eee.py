'''import os
import os.path
import datetime

base_dir = "E:\\git\\jimi10086_test\\data\\"
l = os.listdir(base_dir)
l.sort(key=lambda fn: os.path.getmtime(base_dir + fn) if not os.path.isdir(base_dir + fn) else 0)
d = datetime.datetime.fromtimestamp(os.path.getmtime(base_dir + l[-1]))
# print('最后改动的文件是' + l[-1] + ",时间:" + d.strftime("%Y年%m月%d日 %H时%M分%S秒"))
print(l[-1])'''


def move(n, a, b, c):
    if n == 1:
        print('%s --> %s' % (a, c))
    else:
        move((n - 1), a, c, b)
        move(1, a, b, c)
        move((n - 1), b, a, c)


move(1, 'A', 'B', 'C')
