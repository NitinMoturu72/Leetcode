# 23. Merge k Sorted Lists

# Hard

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        
        nodes.sort()

        res = ListNode(0)
        curr = res
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next
        
        return res.next

#Brute Force Solution
# We first extract all the values from the linked lists into a single list, 
# sort that list, and then create a new linked list from the sorted values.
# The time complexity of this approach is O(n log n) due to the sorting step, where n is the total number of nodes across all linked lists.
# The space complexity is O(n) due to the additional list used to store the node values.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if  not lists or len(lists) == 0:
            return None
        
        while len(lists) >1 :
            mergedLists = []
            for i in range(0,len(lists), 2):
                lst1 = lists[i]
                lst2 = lists[i+1] if i+1 < len(lists) else None

                mergedLists.append(self.mergeLists(lst1,lst2))
            lists = mergedLists
        return lists[0]

                
    def mergeLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next

#Merge Sort Approach
# We can use a divide-and-conquer approach to merge the linked lists.
# In each iteration, we merge pairs of linked lists until only one remains.
# The time complexity is O(n log k), where n is the total number of nodes and k is the number of linked lists.
# The space complexity is O(log k) due to the recursive call stack.