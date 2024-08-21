#!/user/bin/env python3
# -*- coding: utf-8 -*-


# 插入排序：构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
def insertSort(nums):
    """
    """
    n = len(nums)
    for i in range(1, n):   # 默认第一个数已排好序；未排序的数组从下标=1处开始;遍历未排序的数组与已排好序的数组对比，将数插入到合适的位置
        for j in range(i):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


if __name__ == '__main__':
    num_list = [9, 8, 7, 6, 2, 3, 4, 1]
    result = insertSort(num_list)
    print(result)