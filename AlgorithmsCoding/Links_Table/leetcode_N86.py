# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        more_dummy = ListNode(-1)
        more_pointer = more_dummy
        less_dummy = ListNode(-2)
        less_pointer = less_dummy
        pointer = head  # Importance

        while pointer is not None:
            if pointer.val < x:
                less_pointer.next = pointer
                less_pointer = less_pointer.next
            else:
                more_pointer.next = pointer
                more_pointer = more_pointer.next

            # Most importance: 断开原来的链表
            temp = pointer.next
            pointer.next = None
            pointer = temp

        less_pointer.next = more_dummy.next

        return less_dummy.next
