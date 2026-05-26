from typing import Optional


class TreeNode:
    """二叉树节点。

    Attributes:
        val: 节点值。
        left: 左子节点。
        right: 右子节点。
    """

    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        """初始化二叉树节点。

        Args:
            val: 节点值，默认为 0。
            left: 左子节点，默认为 None。
            right: 右子节点，默认为 None。
        """
        self.val = val
        self.left = left
        self.right = right


def inorder(root: Optional[TreeNode]) -> list:
    """二叉树中序遍历（左-根-右）。

    递归访问左子树、根节点、右子树。只需调整拼接顺序即可实现前序或后序遍历。

    Args:
        root: 二叉树根节点。

    Returns:
        中序遍历的节点值列表。

    Example:
        >>> tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        >>> inorder(tree)
        [4, 2, 5, 1, 3]
    """
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