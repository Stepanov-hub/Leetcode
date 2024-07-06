def pre_order(node_p, node_q, fl):
    if node_p is not None and node_q is not None:
        if node_p.val == node_q.val:
            pre_order(node_p.left, node_q.left, fl)
            pre_order(node_p.right, node_q.right, fl)
        else:
            fl[False] = 0
    elif node_p is None and node_q is None:
        pass
    else:
        fl[False] = 0


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        fl = {}
        pre_order(p, q, fl)
        return fl.get(False, True)
