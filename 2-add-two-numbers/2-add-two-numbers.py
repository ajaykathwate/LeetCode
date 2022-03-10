# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        one =''
        
        while l1:
            one+=str(l1.val)
            l1 = l1.next
            
        two = ''
        while l2:
            two+=str(l2.val)
            l2 = l2.next
            
        ans = str(int(one[::-1]) + int(two[::-1]))[::-1]
        
        dummy = curr =  ListNode(0)
        
        for i in ans:
            curr.next = ListNode(val = int(i))
            curr = curr.next
        
        curr.next  = None
        return dummy.next