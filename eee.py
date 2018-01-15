day = '2018-1-12'
print(len(day))
if len(day) == 9:
    if len(day.split('-')[2]) == 1:
        day = day.split('-')[0] + '-' + day.split('-')[1] + "-" + '0' + day.split('-')[2]
        print(day)
    elif len(day.split('-')[1]) == 1:
        day = day.split('-')[0] + '-' + "0" + day.split('-')[1] + "-" + day.split('-')[2]
        print(day)
elif len(day) == 8:
    day = day.split('-')[0] + '-0' + day.split('-')[1] + "-0" + day.split('-')[2]
    print(day)
else:
    print(day)
