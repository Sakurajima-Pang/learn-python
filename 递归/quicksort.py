def quicksort(arr: list) -> list:
    """快速排序，采用分治策略。

    选取第一个元素为基准值（pivot），将剩余元素分为小于等于和大于 pivot 的两组，
    分别递归排序后拼接结果。

    Args:
        arr: 待排序的列表。

    Returns:
        排序后的新列表（非原地排序）。

    Example:
        >>> quicksort([3, 6, 8, 10, 1, 2, 1])
        [1, 1, 2, 3, 6, 8, 10]
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([3, 6, 8, 10, 1, 2, 1]))
# [1, 1, 2, 3, 6, 8, 10]