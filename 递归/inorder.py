"""
二叉树遍历 — 递归天然就是树的“母语”

树的结构本身就是递归的（左子树、右子树），遍历只需按顺序递归。

有趣在哪：三行代码完成中序遍历，前序、后序只是换一下拼接顺序。递归让树的操作变得极度自然。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# 构建一棵简单二叉树:   1
#                    / \
#                   2   3
#                  / \
#                 4   5
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(inorder(tree))   # [4, 2, 5, 1, 3]