#!/user/bin/env python3
# -*- coding: utf-8 -*-


# 希尔排序也是一种插入排序,它是简单插入排序经过改进之后的一个更高效的版本，也称为缩小增量排序
#     不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。
#     希尔排序是把记录按下表的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
def shellSort(nums):
    n = len(nums)
    gap = n // 2
    while gap:
        for i in range(gap, n):
            while i - gap >= 0 and nums[i - gap] > nums[i]:
                nums[i - gap], nums[i] = nums[i], nums[i - gap]
                i -= gap
        gap //= 2


if __name__ == '__main__':
    num_list = [9, 8, 7, 6, 2, 3, 4, 1]
    result = shellSort(num_list)
    print(result)