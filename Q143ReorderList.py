# 143. Reorder List

# Medium

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head

        nodes = []

        while curr:
            nodes.append(curr)
            curr = curr.next

        i = 0
        j = len(nodes) - 1

        while i < j:
            nodes[i].next =  nodes[j]

            i +=1
            if i>=j:
                break

            nodes[j].next = nodes[i]
            j -=1

        nodes[i].next = None       

#Brute force
#We can solve this problem by using a list to store the nodes of the linked list. 
#We can then reorder the nodes in the list and update the next pointers accordingly. 
# The time complexity of this approach is O(n), where n is the number of nodes in the linked list, and 
# the space complexity is also O(n) due to the additional list used to store the nodes.

