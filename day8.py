# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = cur = head
        while fast and fast.next:
            fast = fast.next.next
            cur = cur.next
        return cur

    def O2N_middleNode(self, head: ListNode) -> ListNode:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        res = head
        count = 0
        if length == 1:
            return res
        while res:
            count += 1
            res = res.next
            if count == length // 2:
                return res
