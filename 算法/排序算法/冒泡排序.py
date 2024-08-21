#!/user/bin/env python3
# -*- coding: utf-8 -*-


# 冒泡排序：相邻两个数比较，前一个比后一个数大就交换顺序
def bubbleSort(nums):
    """
    :param nums: 待排序的数组
    :return: 排好序的数组
    """
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


if __name__ == '__main__':
    num_list = [9, 8, 7, 6, 2, 3, 4, 1]
    result = bubbleSort(num_list)
    print(result)
