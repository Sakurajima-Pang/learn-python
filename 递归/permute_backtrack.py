def permute(nums: list) -> list:
    """生成列表的所有全排列（回溯法）。

    通过递归深度优先遍历决策树：每次选择一个未使用的元素加入路径，
    递归完成后撤销选择，直到所有元素都被使用。

    Args:
        nums: 输入列表。

    Returns:
        包含所有排列的列表。

    Example:
        >>> permute([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    result = []

    def backtrack(path: list, remaining: list) -> None:
        """回溯辅助函数。

        Args:
            path: 当前已选择的元素路径。
            remaining: 剩余可选元素列表。
        """
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i + 1:])
            path.pop()

    backtrack([], nums)
    return result

print(permute([1, 2, 3 , 4 , 5]))

# 有趣在哪：递归+回溯让你能“试一下，不行就退回”，
# 这就是很多组合问题、数独、八皇后的核心思想。
