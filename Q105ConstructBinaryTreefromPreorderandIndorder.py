# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Medium

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: mid+1], inorder[: mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
    
# Recursive Approach
# The recursive approach involves selecting the first element of the preorder list as the root of the tree.
# We then find the index of this root value in the inorder list, which allows us to determine the left and right subtrees.
# We recursively build the left and right subtrees using the corresponding slices of the preorder and inorder lists.
# Time complexity: O(n^2) in the worst case, where n is the number of nodes in the tree, due to the slicing of lists and searching for the root in the inorder list.
# Space complexity: O(n) for the recursion stack and the space used to store the tree nodes.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val:idx for index, val in enumerate(inorder)}

        self.pre_idx = 0

        def dfs(l,r):
            if l> r:
                return None
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            mid = indices[root_val]

            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        return dfs(0, len(inorder)-1)

# Hashmap Approach
# The hashmap approach optimizes the search for the root value in the inorder list by using a dictionary to store the indices of each value.
# This allows for O(1) time complexity when looking up the index of the root value.
# We maintain a pointer (pre_idx) to track the current index in the preorder list,
# and we recursively build the left and right subtrees using the indices from the hashmap.
# Time complexity: O(n), where n is the number of nodes in the tree, as we visit each node once.
# Space complexity: O(n) for the recursion stack and the space used to store the tree nodes and the hashmap.