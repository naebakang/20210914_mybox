# File encoding: UTF-8
"""
https://leetcode.com/problems/4sum/
"""

nums = [1, 0, -1, 0, -2, 2]
target = 0

list_total = []
for i in range(0, len(nums)):
    num1 = nums[i]
    for ii in range(0, len(nums)):
        num2 = nums[ii]
        for iii in range(0, len(nums)):
            num3 = nums[iii]
            for iiii in range(0, len(nums)):
                num4 = nums[iiii]

                list_split = [num1, num2, num3, num4]
                list_total.append(list_split)

# 여기서 바로 소트하고 중복 제거

discriminator = nums[:]
list_acknowledgment = []
checker = True
for i in list_total:
    for ii in i:
        try:
            discriminator.remove(ii)
        except:
            checker = False
    if checker is True:
        list_acknowledgment.append(i)

    checker = True
    discriminator = nums[:]

list_check_target = []
for i in range(len(list_acknowledgment)):
    if (sum(list_acknowledgment[i])) == target:
        list_check_target.append(list_acknowledgment[i])

list_check_same = []
for i in list_check_target:
    i.sort()
    add = tuple(i)
    list_check_same.append(add)
list_check_same = list(set(list_check_same))

list_ans = []
for i in list_check_same:
    list_ans.append(list(i))

print(list_ans)
