import re

a = re.search(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',
              '255.101.250.0')
print(a)

b = [{'id': 123, 'name': '张三'}, {'id': 0, 'name': 'lisi', 'name2': 'wangwu'}]
for n in b:
    if n['id'] == 0:
        del (n['name2'])
print(b)

res_data = [{'startLng': 0, 'imei': '987456123012353', 'runTimeSecond': 0, 'endLat': 0, 'avgSpeed': 0, 'endLng': 0,
             'startLat': 0, 'endTime': '2017-08-25 09:12:05', 'distance': 1338812105.90083,
             'startTime': '2017-08-22 14:29:49'},
            {'startLng': 0, 'imei': '868120136573455', 'runTimeSecond': 0, 'endLat': 0, 'avgSpeed': 0, 'endLng': 0,
             'startLat': 0, 'endTime': '2017-08-25 09:20:40', 'distance': 782.943126353093,
             'startTime': '2017-08-21 11:20:10'},
            {'startLng': 0, 'imei': '358740051010725', 'runTimeSecond': 0, 'endLat': 0, 'avgSpeed': 0, 'endLng': 0,
             'startLat': 0, 'endTime': '2017-08-17 18:10:23', 'distance': 1345.98940693375,
             'startTime': '2017-08-14 16:36:23'},
            {'startLng': 0, 'imei': '868120145233604', 'runTimeSecond': 0, 'endLat': 0, 'avgSpeed': 0, 'endLng': 0,
             'startLat': 0, 'endTime': '2017-08-21 14:30:53', 'distance': 40550.4864620702,
             'startTime': '2017-08-09 20:56:05'},
            {'startLng': 0, 'imei': '456123456545678', 'runTimeSecond': 0, 'endLat': 0, 'avgSpeed': 0, 'endLng': 0,
             'startLat': 0, 'endTime': '2017-08-08 15:54:32', 'distance': 39232451.065679,
             'startTime': '2017-08-08 15:49:12'},
            {'startLng': 0, 'imei': '358899055249547', 'runTimeSecond': 0, 'endLat': 0, 'avgSpeed': 0, 'endLng': 0,
             'startLat': 0, 'endTime': '2017-08-07 18:29:56', 'distance': 6833488.64070023,
             'startTime': '2017-08-07 17:05:35'},
            {'startLng': 0, 'imei': '912845678012365', 'runTimeSecond': 0, 'endLat': 0, 'avgSpeed': 0, 'endLng': 0,
             'startLat': 0, 'endTime': '2017-08-25 11:33:03', 'distance': 77193796.1394772,
             'startTime': '2017-08-07 17:01:13'},
            {'startLng': 0, 'imei': '868120161959553', 'runTimeSecond': 0, 'endLat': 0, 'avgSpeed': 0, 'endLng': 0,
             'startLat': 0, 'endTime': '2017-08-24 08:06:00', 'distance': 1555505.82496285,
             'startTime': '2017-08-05 15:31:52'},
            {'startLng': 0, 'imei': '358740056045429', 'runTimeSecond': 0, 'endLat': 0, 'avgSpeed': 0, 'endLng': 0,
             'startLat': 0, 'endTime': '2017-08-16 18:37:02', 'distance': 44834.7955406423,
             'startTime': '2017-08-04 15:54:32'},
            {'startLng': 0, 'imei': '654852658985824', 'runTimeSecond': 0, 'endLat': 0, 'avgSpeed': 0, 'endLng': 0,
             'startLat': 0, 'endTime': '2017-08-09 22:15:40', 'distance': 9458044.20599436,
             'startTime': '2017-08-03 01:29:30'},
            {'startLng': 0, 'imei': '868120167355202', 'runTimeSecond': 0, 'endLat': 0, 'avgSpeed': 0, 'endLng': 0,
             'startLat': 0, 'endTime': '2017-08-24 13:45:17', 'distance': 1422749.25284745,
             'startTime': '2017-08-01 08:01:10'},
            {'startLng': 0, 'imei': '868120167355178', 'runTimeSecond': 0, 'endLat': 0, 'avgSpeed': 0, 'endLng': 0,
             'startLat': 0, 'endTime': '2017-08-25 20:18:33', 'distance': 1343411.9964195,
             'startTime': '2017-08-01 08:00:55'},
            {'startLng': 0, 'imei': '868120161951022', 'runTimeSecond': 0, 'endLat': 0, 'avgSpeed': 0, 'endLng': 0,
             'startLat': 0, 'endTime': '2017-08-24 12:10:15', 'distance': 1348741.4872491,
             'startTime': '2017-08-01 02:45:32'}]
for data in res_data:
    del data['avgSpeed'], data['startLng'], data['imei'], data['runTimeSecond']

print(res_data)

c = '%.3f' % (9875.54587 / 1000)
print(c)
print(type(c))
