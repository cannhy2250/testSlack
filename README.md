# 算法仓库

这个仓库包含了各种算法的实现。

## 快速排序 (Quick Sort)

`quicksort.py` 文件包含了快速排序算法的多种实现：

### 功能特性

- **基础快速排序** (`quicksort_basic`): 递归实现，创建新列表
- **原地快速排序** (`quicksort_inplace`): 节省内存的原地排序
- **随机化快速排序** (`quicksort_randomized`): 避免最坏情况
- **迭代快速排序** (`quicksort_iterative`): 使用栈模拟递归

### 使用方法

```bash
# 运行演示和性能测试
python quicksort.py
```

```python
# 在代码中使用
from quicksort import quicksort_basic, quicksort_inplace

# 基础用法
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quicksort_basic(arr)
print(sorted_arr)  # [11, 12, 22, 25, 34, 64, 90]

# 原地排序
arr = [64, 34, 25, 12, 22, 11, 90]
quicksort_inplace(arr)
print(arr)  # [11, 12, 22, 25, 34, 64, 90]
```

### 算法特点

- **时间复杂度**: O(n log n) 平均情况，O(n²) 最坏情况
- **空间复杂度**: O(log n) 平均情况，O(n) 最坏情况
- **稳定性**: 不稳定排序
- **原地性**: 支持原地排序（`quicksort_inplace` 版本）
