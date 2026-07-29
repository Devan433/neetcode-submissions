# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        value1=[]
        value2=[]
        def dfs(node,values):
            if not node :
                values.append(None)
                return 0
            values.append(node.val)
            dfs(node.left,values)
            dfs(node.right,values)
        dfs(p,value1)
        dfs(q,value2)
        return value1==value2