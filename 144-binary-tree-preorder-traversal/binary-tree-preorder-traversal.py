# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result=[]
        self.preorder(root,result)
        return result
    def preorder(self,node,result):
        if not node:
            return 
        result.append(node.val)
        self.preorder(node.left,result)
        self.preorder(node.right,result)


        