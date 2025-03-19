# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result=[]
        self.postorder(root,result)
        return result
    def postorder(self,node,result):
        if not node:
            return
        self.postorder(node.left,result)
        self.postorder(node.right,result)
        result.append(node.val)


        

        