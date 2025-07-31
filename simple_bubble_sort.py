#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化版冒泡排序 - 适合初学者
=============================

冒泡排序的核心思想：
1. 比较相邻的两个元素
2. 如果前面的元素比后面的大，就交换它们
3. 重复这个过程，直到整个数组排序完成

就像气泡从水底冒到水面一样，大的数字会"冒泡"到数组的末尾
"""

def bubble_sort(arr):
    """
    冒泡排序 - 升序排列
    
    参数:
        arr: 要排序的数字列表
    
    返回:
        排序后的列表
    """
    # 复制数组，避免修改原数组
    numbers = arr.copy()
    n = len(numbers)
    
    # 外层循环：控制排序的轮数
    for i in range(n):
        print(f"\n=== 第 {i+1} 轮排序 ===")
        
        # 内层循环：进行相邻元素的比较和交换
        for j in range(0, n - i - 1):
            print(f"比较 {numbers[j]} 和 {numbers[j+1]}", end=" ")
            
            # 如果前面的数比后面的数大，就交换它们
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                print(f"→ 交换！现在是: {numbers}")
            else:
                print("→ 不需要交换")
        
        print(f"第 {i+1} 轮结束: {numbers}")
    
    return numbers


def simple_bubble_sort(arr):
    """
    最简单的冒泡排序实现 - 无调试输出
    """
    numbers = arr.copy()
    n = len(numbers)
    
    # 外层循环控制轮数
    for i in range(n):
        # 内层循环进行比较和交换
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # 交换两个元素
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    
    return numbers


# 测试代码
if __name__ == "__main__":
    print("🔄 简化版冒泡排序演示")
    print("=" * 40)
    
    # 测试数据
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"原始数组: {test_data}")
    
    # 详细演示版本
    print("\n📝 详细步骤演示:")
    result = bubble_sort(test_data)
    print(f"\n✅ 最终结果: {result}")
    
    # 简单版本测试
    print("\n" + "=" * 40)
    print("🚀 简单版本测试:")
    
    test_cases = [
        [5, 2, 8, 1, 9],
        [3, 1, 4, 1, 5],
        [9, 8, 7, 6, 5],
        [1, 2, 3, 4, 5]
    ]
    
    for i, case in enumerate(test_cases, 1):
        sorted_result = simple_bubble_sort(case)
        print(f"测试 {i}: {case} → {sorted_result}")
    
    print("\n💡 冒泡排序小贴士:")
    print("• 每一轮都会把最大的数'冒泡'到最后")
    print("• 时间复杂度是 O(n²)，适合小数据量")
    print("• 算法稳定，相同元素的相对位置不会改变")
    print("• 实现简单，是学习排序算法的好起点！")