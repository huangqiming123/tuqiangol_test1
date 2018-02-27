# 现有资源
total = 100

big_chicken_male = 5
big_chicken_female = 3
small_chicken = 1

result = []
temp = []
# 购买公鸡数量
for x in range(0, total // big_chicken_male + 1):
    # 购买母鸡数量
    for y in range(0, total // big_chicken_female + 1):
        # 购买小鸡数量
        for z in range(0, total // small_chicken + 1):
            sum = big_chicken_male * x + big_chicken_female * y + small_chicken * z
            temp.append([x, y, z])
            if sum > total:
                temp.pop()
                if temp:
                    result.append(temp.pop())
                    temp = []
                    break
            elif sum == total:
                result.append(temp.pop())
                temp = []
                break
for i in result:
    print("购买公鸡: {0}, 购买母鸡: {1}, 购买小鸡: {2}".format(i[0], i[1], i[2]))
print("总计购买方案: {0}种".format(len(result)))
