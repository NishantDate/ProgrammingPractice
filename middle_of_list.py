from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        two_step = head
        one_step = head
        counter = 0
        while(one_step):
            if counter%2:
                two_step = two_step.next
            one_step = one_step.next
            counter += 1

        return two_step