class myException(Exception):
    def __init__(self, massage):
        Exception.__init__(self)
        self.massage = massage


a = input('please input a number:')
if int(a) > 10:
    try:
        raise myException('my exception is a raised')
    except myException:
        print(myException)
