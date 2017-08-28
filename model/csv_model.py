import csv

# 定义csv文件存放路径
csv_file = open(r"D:\git\giiso\Data\user_login.csv", 'r', encoding='utf8')

# 用csv的reader（）方法读取csv文件的数据
csv_data = csv.reader(csv_file)

# 遍历csv数据

# 判断is_header
is_header = True
for row in csv_data:
    if is_header:
        is_header = False
        continue

    # 将csv文件中的每一列数据存到dict中
    user_to_login = {
        "account": "row[0]",
        "password": "row[1]"
    }

csv_file.close()
