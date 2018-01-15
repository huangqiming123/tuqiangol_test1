def call(i):
    return i * 2


def test_yield(n):
    for i in range(n):
        yield call(i)
        print("i = ", i)
    print('do anything')


for n in test_yield(3):
    print(n)

for m in range(10):
    print(m, end=' ')
print()
for m in range(1, 10):
    print(m, end=' ')
print()
for m in range(1, 10, 2):
    print(m, end=' ')

# range(start,end,step)
