data = [
    {"imei": "424111111124478", "totalDistiance": 4.10179878E8, "totalTime": 4920},
    {"imei": "888001234567894", "totalDistiance": 4009, "totalTime": 2045},
    {"imei": "912845678012365", "totalDistiance": 1.453394059E9, "totalTime": 16910},
    {"imei": "868120111111120", "totalDistiance": 1.00099257E8, "totalTime": 13823},
    {"imei": "868120136573455", "totalDistiance": 37635, "totalTime": 76028},
    {"imei": "868261010000064", "totalDistiance": 4.2992361E7, "totalTime": 4783},
    {"imei": "868120111111122", "totalDistiance": 1.26525845E8, "totalTime": 1488},
    {"imei": "868950020085624", "totalDistiance": 1.469932E7, "totalTime": 733},
    {"imei": "987456123012353", "totalDistiance": 1.160140401E9, "totalTime": 23271},
    {"imei": "567897897897903", "totalDistiance": 4.0850547E7, "totalTime": 394},
    {"imei": "868120145233604", "totalDistiance": 17070, "totalTime": 315262},
    {"imei": "358740051669389", "totalDistiance": 5142899, "totalTime": 77510}
]
total = 0
for datas in data:
    total += datas['totalDistiance']
print(total / 1000)
