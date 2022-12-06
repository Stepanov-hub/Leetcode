from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode(0)
        final = result
        one_point = 0

        while l1 is not None or l2 is not None or one_point == 1:

            if l1 is None and l2 is None:
                new = one_point
            elif l1 is None:
                new = l2.val + one_point
                l2 = l2.next
            elif l2 is None:
                new = l1.val + one_point
                l1 = l1.next
            else:
                new = l1.val + l2.val + one_point
                l1 = l1.next
                l2 = l2.next

            if new >= 10:
                one_point = 1
                result.val = new % 10
            else:
                one_point = 0
                result.val = new % 10

            if l1 is not None or l2 is not None or one_point == 1:
                result.next = ListNode(0)
                result = result.next

        return final
