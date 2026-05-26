# 生成全排列 — 回溯法中的递归
# 给定列表 [1,2,3]，生成所有排列。递归在这里做的是决策树的深度优先遍历。
def permute(nums):
    result = []
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])   # 找到一个排列
            return
        for i in range(len(remaining)):
            # 做选择
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            # 撤销选择（回溯）
            path.pop()
    
    backtrack([], nums)
    return result

print(permute([1, 2, 3 , 4 , 5]))

# 有趣在哪：递归+回溯让你能“试一下，不行就退回”，
# 这就是很多组合问题、数独、八皇后的核心思想。
