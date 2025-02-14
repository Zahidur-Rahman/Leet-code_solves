# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n=0
        stack=[]
        curr=root
        
        while curr or stack:
            while curr:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()    
            n+=1
            
            if n==k:
                return cur.val
            
                
                
                