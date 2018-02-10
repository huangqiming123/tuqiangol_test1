from xlwt import *


def write_excel(sheet_name, l_data):
    # 写入数据到excel方法t
    # 指定文件打开方式utf8
    file = Workbook(encoding='utf-8')
    table = file.add_sheet(sheet_name)

    '''num = [a for a in data]
    print('mum',num)
    num.sort()

    for x in num:
        print('x',x)
        t = [int(x)]
        for a in data[x]:
            t.append(a)
        l_data.append(t)
    print(l_data)'''

    for i, p in enumerate(l_data):
        for j, q in enumerate(p):
            table.write(i, j, q)
    file.save(sheet_name + '.xlsx')
