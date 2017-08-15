# --*-- coding:utf-8 --*--
import xlrd


def open_excel(file):
    try:
        excel_file = xlrd.open_workbook(file)
        return excel_file
    except:
        print('找不到文件')


def read_excel_file_by_index(file, col_name_index=0, by_index=0):
    excel_file = open_excel(file)
    # table = excel_file.sheets[by_index]
    table = excel_file.sheet_by_index(by_index)
    # 列数
    number_rows = table.nrows
    # 每一列总共有多少个值
    colnames = table.row_values(col_name_index)

    list = []
    for rownum in range(1, number_rows):

        row = table.row_values(rownum)
        if row:
            data = {}
            for i in range(len(colnames)):
                data[colnames[i]] = row[i]
            list.append(data)
    return list


def read_excel_file_by_name(file, col_name_index=0, by_name='Sheet1'):
    excel_file = open_excel(file)
    table = excel_file.sheet_by_name(by_name)
    number_rows = table.nrows
    colnames = table.row_values(col_name_index)

    list = []
    for rownum in range(1, number_rows):
        row = table.row_values(rownum)
        if row:
            data = {}
            for i in range(len(colnames)):
                data[colnames[i]] = row[i]
            list.append(data)
    return list


def main():
    tables = read_excel_file_by_index('read_excel_demo.xls')
    print(tables)

    tables = read_excel_file_by_name('read_excel_demo.xls')
    print(tables)


if __name__ == '__main__':
    main()
