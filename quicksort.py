#!/usr/bin/env python3
"""
快速排序 (Quick Sort) 实现
=======================

快速排序是一种高效的分治排序算法，平均时间复杂度为 O(n log n)。

作者: AI Assistant
日期: 2024
"""

import random
from typing import List, TypeVar

T = TypeVar('T')


def quicksort_basic(arr: List[T]) -> List[T]:
    """
    基础快速排序实现 (递归版本)
    
    Args:
        arr: 待排序的列表
        
    Returns:
        排序后的新列表
        
    Time Complexity: O(n log n) 平均情况, O(n²) 最坏情况
    Space Complexity: O(log n) 平均情况, O(n) 最坏情况
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort_basic(left) + middle + quicksort_basic(right)


def quicksort_inplace(arr: List[T], low: int = 0, high: int = None) -> None:
    """
    原地快速排序实现 (更节省内存)
    
    Args:
        arr: 待排序的列表 (会被直接修改)
        low: 起始索引
        high: 结束索引
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # 分区操作，返回基准元素的正确位置
        pivot_index = partition(arr, low, high)
        
        # 递归排序基准元素左右两部分
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)


def partition(arr: List[T], low: int, high: int) -> int:
    """
    分区函数 - Lomuto 分区方案
    
    选择最后一个元素作为基准，将数组分为两部分：
    - 左部分：所有小于基准的元素
    - 右部分：所有大于等于基准的元素
    
    Args:
        arr: 数组
        low: 起始索引
        high: 结束索引
        
    Returns:
        基准元素的最终位置
    """
    pivot = arr[high]  # 选择最后一个元素作为基准
    i = low - 1  # 小于基准元素区域的右边界
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort_randomized(arr: List[T]) -> List[T]:
    """
    随机化快速排序 (避免最坏情况)
    
    通过随机选择基准元素来避免最坏情况的发生
    
    Args:
        arr: 待排序的列表
        
    Returns:
        排序后的新列表
    """
    if len(arr) <= 1:
        return arr
    
    # 随机选择基准元素
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort_randomized(left) + middle + quicksort_randomized(right)


def quicksort_iterative(arr: List[T]) -> None:
    """
    迭代版本的快速排序 (使用栈模拟递归)
    
    Args:
        arr: 待排序的列表 (会被直接修改)
    """
    if len(arr) <= 1:
        return
    
    # 使用栈来模拟递归调用
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pivot_index = partition(arr, low, high)
            
            # 将子数组的边界压入栈中
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))


def demo():
    """演示快速排序的各种实现"""
    print("=== 快速排序演示 ===\n")
    
    # 测试数据
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    for i, original in enumerate(test_cases, 1):
        print(f"测试用例 {i}: {original}")
        
        # 基础快速排序
        result1 = quicksort_basic(original.copy())
        print(f"基础快速排序:     {result1}")
        
        # 原地快速排序
        arr2 = original.copy()
        quicksort_inplace(arr2)
        print(f"原地快速排序:     {arr2}")
        
        # 随机化快速排序
        result3 = quicksort_randomized(original.copy())
        print(f"随机化快速排序:   {result3}")
        
        # 迭代快速排序
        arr4 = original.copy()
        quicksort_iterative(arr4)
        print(f"迭代快速排序:     {arr4}")
        
        print("-" * 50)


def performance_test():
    """性能测试"""
    import time
    
    print("\n=== 性能测试 ===")
    
    # 生成测试数据
    sizes = [1000, 5000, 10000]
    
    for size in sizes:
        print(f"\n数组大小: {size}")
        
        # 随机数组
        random_arr = [random.randint(1, 1000) for _ in range(size)]
        
        # 测试基础快速排序
        arr1 = random_arr.copy()
        start_time = time.time()
        quicksort_basic(arr1)
        time1 = time.time() - start_time
        print(f"基础快速排序:   {time1:.4f} 秒")
        
        # 测试原地快速排序
        arr2 = random_arr.copy()
        start_time = time.time()
        quicksort_inplace(arr2)
        time2 = time.time() - start_time
        print(f"原地快速排序:   {time2:.4f} 秒")
        
        # 测试迭代快速排序
        arr3 = random_arr.copy()
        start_time = time.time()
        quicksort_iterative(arr3)
        time3 = time.time() - start_time
        print(f"迭代快速排序:   {time3:.4f} 秒")


if __name__ == "__main__":
    # 运行演示
    demo()
    
    # 运行性能测试
    performance_test()
    
    print("\n=== 算法特点 ===")
    print("✓ 时间复杂度: O(n log n) 平均, O(n²) 最坏")
    print("✓ 空间复杂度: O(log n) 平均, O(n) 最坏")
    print("✓ 不稳定排序")
    print("✓ 原地排序 (原地版本)")
    print("✓ 分治算法")