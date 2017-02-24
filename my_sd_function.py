import math

# 定義自訂函數
def my_std(input_list):
    '計算標準差' # docstrings
    def my_sum(input_list):
        '計算總和'
        temp_sum = 0
        for i in input_list:
            temp_sum += i
        return temp_sum
    def my_length(input_list):
        '計算個數'
        temp_length = 0
        for i in input_list:
            temp_length += 1
        return temp_length
    def my_square_sum(input_list):
        '計算平方和' # docstrings
        temp_sq_sum = 0
        for i in input_list:
            temp_sq_sum += i**2
        return temp_sq_sum
    return math.sqrt((my_square_sum(input_list)/my_length(input_list))-(my_sum(input_list) / my_length(input_list))**2)

# 呼叫自訂函數
one_to_10 = range(1, 11)
print(my_std(one_to_10))