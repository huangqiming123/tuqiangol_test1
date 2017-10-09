def min(a, b):
    sum_a = sum(a)
    sum_b = sum(b)
    chang_sum = []
    for i in range(len(a)):
        for j in range(len(b)):
            sum_change = (sum_a - a[i] + b[j]) - (sum_b + a[i] - b[j])
            print('a中的第%s元素和b中的第%s元素交换后，两个序列的差为：%s' % (i, j, sum_change))
            chang_sum.append(sum_change)


a = [99, 2, 2, 10]
b = [100, 5, 5, 3]
min(a, b)
