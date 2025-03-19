# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self,root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result=[]
        self.level(root,result,0)
        return result
    def level(self,node,result,level):
        # while i<n
        if not node:
            return
        if len(result)==level:
            result.append([])
        result[level].append(node.val)
        self.level(node.left,result,level+1)
        self.level(node.right,result,level+1)
            
            