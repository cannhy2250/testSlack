#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
冒泡排序 (Bubble Sort) 实现
================================

冒泡排序是一种简单的排序算法，它重复地遍历要排序的列表，
比较相邻的元素并交换它们（如果它们的顺序错误）。

时间复杂度：
- 最好情况：O(n) - 当数组已经排序时
- 平均情况：O(n²)
- 最坏情况：O(n²)

空间复杂度：O(1) - 原地排序

作者：Python学习者
日期：2024年
"""

def bubble_sort_basic(arr):
    """
    基础版冒泡排序
    
    Args:
        arr (list): 待排序的列表
    
    Returns:
        list: 排序后的列表
    """
    # 创建副本，避免修改原数组
    arr = arr.copy()
    n = len(arr)
    
    # 外层循环控制排序轮数
    for i in range(n):
        # 内层循环进行相邻元素比较和交换
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


def bubble_sort_optimized(arr):
    """
    优化版冒泡排序 - 添加提前终止条件
    
    如果在某一轮中没有发生交换，说明数组已经有序，可以提前结束
    
    Args:
        arr (list): 待排序的列表
    
    Returns:
        list: 排序后的列表
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        # 标记本轮是否发生交换
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果本轮没有交换，说明已经排序完成
        if not swapped:
            break
    
    return arr


def bubble_sort_with_steps(arr):
    """
    带步骤显示的冒泡排序 - 用于学习和调试
    
    Args:
        arr (list): 待排序的列表
    
    Returns:
        list: 排序后的列表
    """
    arr = arr.copy()
    n = len(arr)
    
    print(f"初始数组: {arr}")
    print("-" * 40)
    
    for i in range(n):
        print(f"第 {i + 1} 轮排序:")
        swapped = False
        
        for j in range(0, n - i - 1):
            print(f"  比较 {arr[j]} 和 {arr[j + 1]}", end="")
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f" -> 交换: {arr}")
            else:
                print(f" -> 不交换: {arr}")
        
        if not swapped:
            print(f"  本轮无交换，排序完成！")
            break
        
        print(f"第 {i + 1} 轮结束: {arr}")
        print("-" * 40)
    
    return arr


def bubble_sort_descending(arr):
    """
    降序冒泡排序
    
    Args:
        arr (list): 待排序的列表
    
    Returns:
        list: 降序排序后的列表
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            # 改变比较条件实现降序
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


def bubble_sort_generic(arr, reverse=False, key=None):
    """
    通用冒泡排序 - 支持自定义排序规则
    
    Args:
        arr (list): 待排序的列表
        reverse (bool): 是否降序排序，默认False（升序）
        key (function): 自定义比较函数，默认None
    
    Returns:
        list: 排序后的列表
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            # 获取比较值
            val1 = key(arr[j]) if key else arr[j]
            val2 = key(arr[j + 1]) if key else arr[j + 1]
            
            # 根据reverse参数决定比较方向
            should_swap = (val1 > val2) if not reverse else (val1 < val2)
            
            if should_swap:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


def performance_test():
    """
    性能测试函数 - 比较不同版本的冒泡排序性能
    """
    import time
    import random
    
    # 生成测试数据
    sizes = [100, 500, 1000]
    
    print("冒泡排序性能测试")
    print("=" * 50)
    
    for size in sizes:
        # 生成随机数组
        test_arr = [random.randint(1, 1000) for _ in range(size)]
        
        print(f"\n数组大小: {size}")
        print("-" * 30)
        
        # 测试基础版本
        arr_copy = test_arr.copy()
        start_time = time.time()
        bubble_sort_basic(arr_copy)
        basic_time = time.time() - start_time
        
        # 测试优化版本
        arr_copy = test_arr.copy()
        start_time = time.time()
        bubble_sort_optimized(arr_copy)
        optimized_time = time.time() - start_time
        
        print(f"基础版本: {basic_time:.4f} 秒")
        print(f"优化版本: {optimized_time:.4f} 秒")
        print(f"性能提升: {((basic_time - optimized_time) / basic_time * 100):.2f}%")


def main():
    """
    主函数 - 演示各种冒泡排序的使用
    """
    print("🔄 Python 冒泡排序演示")
    print("=" * 50)
    
    # 测试数据
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1],  # 单元素
        [],   # 空数组
        [3, 3, 3, 3],  # 重复元素
        [1, 2, 3, 4, 5],  # 已排序
        [5, 4, 3, 2, 1]   # 逆序
    ]
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\n📊 测试用例 {i}: {arr}")
        print("-" * 30)
        
        if arr:  # 非空数组才进行排序
            # 基础冒泡排序
            sorted_arr = bubble_sort_basic(arr)
            print(f"基础排序结果: {sorted_arr}")
            
            # 优化冒泡排序
            optimized_arr = bubble_sort_optimized(arr)
            print(f"优化排序结果: {optimized_arr}")
            
            # 降序排序
            desc_arr = bubble_sort_descending(arr)
            print(f"降序排序结果: {desc_arr}")
        else:
            print("空数组，无需排序")
    
    # 演示带步骤的排序
    print("\n🎯 详细步骤演示")
    print("=" * 50)
    demo_arr = [64, 34, 25, 12, 22]
    bubble_sort_with_steps(demo_arr)
    
    # 演示通用排序
    print("\n🚀 通用排序演示")
    print("=" * 50)
    
    # 按字符串长度排序
    words = ["python", "java", "c", "javascript", "go"]
    print(f"原始单词列表: {words}")
    sorted_by_length = bubble_sort_generic(words, key=len)
    print(f"按长度排序: {sorted_by_length}")
    
    # 按字典序降序排序
    sorted_desc = bubble_sort_generic(words, reverse=True)
    print(f"按字典序降序: {sorted_desc}")
    
    # 数字按绝对值排序
    numbers = [-5, 3, -1, 4, -2]
    print(f"\n原始数字列表: {numbers}")
    sorted_by_abs = bubble_sort_generic(numbers, key=abs)
    print(f"按绝对值排序: {sorted_by_abs}")
    
    # 性能测试
    print("\n⚡ 性能测试")
    print("=" * 50)
    performance_test()
    
    # 算法分析
    print("\n📈 算法分析")
    print("=" * 50)
    print("冒泡排序特点：")
    print("✅ 实现简单，容易理解")
    print("✅ 原地排序，空间复杂度O(1)")
    print("✅ 稳定排序算法")
    print("❌ 时间复杂度较高O(n²)")
    print("❌ 不适合大数据集")
    print("\n适用场景：")
    print("• 数据量较小的情况")
    print("• 教学和学习算法")
    print("• 需要稳定排序的简单场景")


if __name__ == "__main__":
    main()