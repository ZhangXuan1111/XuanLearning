#!/user/bin/env python3
# -*- coding: utf-8 -*-


# 选择排序：每次都在未排序的数组中找最小值，将其放进已排好序的末尾
def selectSort(nums):
    """
    :param nums: 待排序的数组
    :return: 排好序的数组
    """
    for i in range(len(nums)):
        min_num = nums[i]  # 假设第一个元素是最小值
        if i < len(nums) - 1:
            for j in range(i + 1, len(nums)):
                if nums[j] < min_num:
                    min_num = nums[j]
                    nums[i], nums[j] = nums[j], nums[i]
    return nums

if __name__ == '__main__':
    num_list = [9, 8, 7, 6, 2, 3, 4, 1]
    result = selectSort(num_list)
    print(result)