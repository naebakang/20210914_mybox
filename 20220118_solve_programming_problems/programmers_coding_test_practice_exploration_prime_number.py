# # File encoding: UTF-8
#
# ex_numbers = '17'
# ex_return = 3
#
# # split
# input_split = []
# for i in ex_numbers:
#     input_split.append(i)
#
# # total number
# total_number = []
# for i in range(len(ex_numbers)):
#
# Index
# New_index_list = []
# for i in index_list:
#     if i == len:
#         index_list
#         New_index_list.append(0)
#     else:
#         New_index_list.append(int(i) + 1)
#
#     Index_list = New_index_list
#
#
# Split_num_list = []
# for i in range(최초i):
#
#     for ii in range(len(index_list)):
#         Num = ''
#         for iii in range(i):
#             Num = Num + numlist[indexlist[ii]]
#
#     Split_num_list.append((Num))
#
# for i in range
# 여기서 index update 하고
# 중복 제거

# 앞에 0 제거

# 소수 찾기

# 문자를 숫자로 변환 하는 것 주의
# 소수 체크 하는 함수 별도로 제작
# 맨앞에 0이 있는 경우 오류 발생하니까 주의 필요 어떻게 거를지 생각해야함
# 만들 수 있는 모든 수를 다 생각해놔야 한다


def get_num_and_list(index, total_paper_list):
    index_list = list(range(len(total_paper_list)))
    decreased_list = []
    for i in index_list:
        if i == index:
            pass
        else:
            decreased_list.append(total_paper_list[i])
    num = total_paper_list[index]

    return num, decreased_list


total_paper_list = ['1', '2', '3', '4']
for i in range(len(total_paper_list)):
    num, decreased_list = get_num_and_list(index=i, total_paper_list=total_paper_list)
    for ii in decreased_list:
        print(num + str(ii))


    # print(num)

