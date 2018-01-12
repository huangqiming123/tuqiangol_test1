def function_01(flag, *args):
    print('flag', flag)
    for value in args:
        print(value)


function_01('aaa', 1, 'fas')


def function_02(flag, **kwargs):
    print(flag)
    for key in kwargs:
        print(key, kwargs[key])
