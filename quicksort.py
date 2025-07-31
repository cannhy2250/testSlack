def quicksort(arr):
    """
    快速排序算法实现
    
    Args:
        arr: 待排序的数组
    
    Returns:
        排序后的数组
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    原地快速排序实现（更节省内存）
    
    Args:
        arr: 待排序的数组
        low: 起始索引
        high: 结束索引
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # 分区操作，返回基准元素的正确位置
        pivot_index = partition(arr, low, high)
        
        # 递归排序基准左边和右边的子数组
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    分区函数，将数组分为小于和大于基准的两部分
    
    Args:
        arr: 数组
        low: 起始索引
        high: 结束索引
    
    Returns:
        基准元素的最终位置
    """
    pivot = arr[high]  # 选择最后一个元素作为基准
    i = low - 1  # 较小元素的索引
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def test_quicksort():
    """测试快速排序算法"""
    # 测试用例
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    print("快速排序测试结果：")
    print("=" * 50)
    
    for i, arr in enumerate(test_cases):
        original = arr.copy()
        
        # 测试函数式快速排序
        sorted_arr1 = quicksort(arr.copy())
        
        # 测试原地快速排序
        arr_copy = arr.copy()
        quicksort_inplace(arr_copy)
        
        print(f"测试用例 {i + 1}:")
        print(f"原数组:     {original}")
        print(f"函数式排序: {sorted_arr1}")
        print(f"原地排序:   {arr_copy}")
        print(f"结果一致:   {sorted_arr1 == arr_copy}")
        print("-" * 30)


if __name__ == "__main__":
    test_quicksort()