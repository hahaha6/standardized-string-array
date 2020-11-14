# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from functools import reduce


def set_capitalize(array):
    # 将输入数组转为字符串
        set_string= [str(i) for i in array]
    # 将其转换为标准形式
        string_array = [str.capitalize() for str in set_string]
        print(string_array)

test_set_string = ['amb', 'hbt', 'mab']
set_capitalize(test_set_string)
def Continuous_multiplication(array):
    #将输入数组转换为数字
    num_array = [int(ele) for ele in array]
    print(reduce(lambda multipler,multiplcand:multipler*multiplcand, num_array))

test_num_array = [1,2,4,7,9]
Continuous_multiplication(test_num_array)
