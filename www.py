def input_four_number():
    number = []
    n = 1
    while 1:
        a = input('请输入第%s个数字：' % n)
        if a.isdigit():
            number.append(int(a))
            n += 1
            if len(number) == 4:
                break
    return number


def math(list):
    return list[0] + list[1] - list[2] * list[3]


print(math(input_four_number()))
