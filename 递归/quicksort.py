"""
快速排序 — 分治法的优雅体现

每次选一个基准值，将数组分为“比它小的”和“比它大的”，再递归排序两边。

有趣在哪：一句 quicksort(left) + [pivot] + quicksort(right) 就完成了排序，
把“分而治之”的思想变成了直观可读的代码。

"""
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([3, 6, 8, 10, 1, 2, 1]))
# [1, 1, 2, 3, 6, 8, 10]