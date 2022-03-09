# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, next = head)
        slow = dummy
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                slow.next = head.next
            else:
                slow = slow.next
            head = head.next
        return dummy.next
        
        
        
        
        
# Naive Approach

# temp = []
#        cur = head
#        while cur:
#             temp.append(cur.val)
#             cur = cur.next

#         c = Counter(temp)
#         temp = [k for k, v in c.items() if v == 1]

#         dummy = cur = ListNode()

#         for i in temp:
#             cur.next = ListNode(i)
#             cur = cur.next

#         return dummy.next
