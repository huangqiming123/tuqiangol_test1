from model.write_excel import write_excel

data = [{'stopTimes': 0, 'imei': '868120137194665', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 12, 'imei': '358740051198280', 'overSpeedTimes': 0, 'mileage': 40745},
        {'stopTimes': 10, 'imei': '358740051181674', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '654123654123654', 'overSpeedTimes': 0, 'mileage': 51509553},
        {'stopTimes': 0, 'imei': '868120136491609', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '424111111124478', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '868120166737418', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '111111111111112', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '860123456788888', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '358740051669819', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 29, 'imei': '358740051198314', 'overSpeedTimes': 0, 'mileage': 13744},
        {'stopTimes': 0, 'imei': '365412589658745', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '868120111111120', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '868120148373845', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '365412589658744', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '424111111124522', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '912845678012370', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '860116170500006', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '868120111111119', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '868120136573455', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '519876810593042', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '912845678012371', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '868261010000064', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '867597011453278', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '868120111111122', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '567897897897894', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '912345678984444', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '358899055249547', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '808120137883051', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '987456123012353', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 2, 'imei': '868120111111118', 'overSpeedTimes': 0, 'mileage': 9653681},
        {'stopTimes': 47, 'imei': '358740051198322', 'overSpeedTimes': 0, 'mileage': 13110},
        {'stopTimes': 0, 'imei': '519876810593041', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '868120111111124', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '987456123012358', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '868120111111117', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '868120145148729', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 3, 'imei': '868120111111116', 'overSpeedTimes': 0, 'mileage': 9494132},
        {'stopTimes': 116, 'imei': '868120145233604', 'overSpeedTimes': 0, 'mileage': 209},
        {'stopTimes': 0, 'imei': '567897897897902', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '358740051669389', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '868120136505176', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '912845678012368', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 0, 'imei': '567897897897895', 'overSpeedTimes': 0, 'mileage': 0},
        {'stopTimes': 2, 'imei': '868120111111123', 'overSpeedTimes': 0, 'mileage': 0}]
data3 = [['序号', 'imei', '停留次数', '超速次数', '总里程数']]
for n, e in enumerate(data):
    data2 = [
        (n + 1), e['imei'], e['stopTimes'], e['overSpeedTimes'], e['mileage']
    ]
    data3.append(data2)
print(data3)
write_excel('aaa', data3)
