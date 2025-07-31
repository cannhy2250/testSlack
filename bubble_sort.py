def bubble_sort(arr):
    """
    冒泡排序算法实现
    时间复杂度: O(n²)
    空间复杂度: O(1)
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    """
    n = len(arr)
    
    # 外层循环控制排序轮数
    for i in range(n):
        # 标记本轮是否有元素交换，用于优化
        swapped = False
        
        # 内层循环进行相邻元素比较和交换
        # 每轮排序后，最大的元素会"冒泡"到末尾
        for j in range(0, n - i - 1):
            # 如果前面的元素大于后面的元素，则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果本轮没有交换，说明数组已经有序，可以提前结束
        if not swapped:
            break
    
    return arr


def bubble_sort_verbose(arr):
    """
    带详细过程输出的冒泡排序
    """
    print(f"原始数组: {arr}")
    n = len(arr)
    
    for i in range(n):
        print(f"\n第 {i + 1} 轮排序:")
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
            print("  本轮无交换，排序完成！")
            break
        else:
            print(f"  第 {i + 1} 轮结束: {arr}")
    
    print(f"\n最终结果: {arr}")
    return arr


# 测试示例
if __name__ == "__main__":
    # 测试用例1: 普通数组
    print("=" * 50)
    print("测试用例1: 普通数组")
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    result1 = bubble_sort(test_arr1.copy())
    print(f"原数组: {[64, 34, 25, 12, 22, 11, 90]}")
    print(f"排序后: {result1}")
    
    # 测试用例2: 已排序数组
    print("\n" + "=" * 50)
    print("测试用例2: 已排序数组")
    test_arr2 = [1, 2, 3, 4, 5]
    result2 = bubble_sort(test_arr2.copy())
    print(f"原数组: {[1, 2, 3, 4, 5]}")
    print(f"排序后: {result2}")
    
    # 测试用例3: 逆序数组
    print("\n" + "=" * 50)
    print("测试用例3: 逆序数组")
    test_arr3 = [5, 4, 3, 2, 1]
    result3 = bubble_sort(test_arr3.copy())
    print(f"原数组: {[5, 4, 3, 2, 1]}")
    print(f"排序后: {result3}")
    
    # 测试用例4: 包含重复元素
    print("\n" + "=" * 50)
    print("测试用例4: 包含重复元素")
    test_arr4 = [3, 7, 3, 1, 7, 2]
    result4 = bubble_sort(test_arr4.copy())
    print(f"原数组: {[3, 7, 3, 1, 7, 2]}")
    print(f"排序后: {result4}")
    
    # 详细过程演示
    print("\n" + "=" * 50)
    print("详细排序过程演示:")
    demo_arr = [5, 2, 8, 1, 9]
    bubble_sort_verbose(demo_arr.copy())