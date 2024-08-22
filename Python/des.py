#!/user/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

# 2、如何在一个函数内部修改全局变量?

# a = 3
#
# def mod():
#     global a
#     a = 4
#     return a
#
#
# res = mod()
# print(res)

# 字典合并
# dict1 = {"name":"zhangsan", "test":"0821"}
# del dict1["test"]
# print(dict1)
# dict2 = {"age": 18}
# dict1.update(dict2)
# print(dict1)

# 列表［1,2,3,4,5］请使用 map 函数输出，并使用列表推导式输出大于10的数

# def dealNum(x):
#     return x * x
#
# if __name__ == '__main__':
#     nums = [1, 2, 3, 4, 5]
#     result = map(dealNum, nums)
#     filterNum = [num for num in list(result) if num > 10]
#     print(filterNum)

# a = [1,2,"hello",['python', 'C++']]
# b = a
# print(a is b)

# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#
#     return wrapper
#
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
#
# from functools import reduce
#
#
# def f2(x, y):
#     return x * 10 + y
#
#
# nums = [1, 2, 3, 4, 6]
# result = reduce(f2, nums)
# print(result)

a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num for num in a if num%2 > 0 ]
print(result)
print(4%2)