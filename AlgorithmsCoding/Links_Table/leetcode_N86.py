# Definition for singly-linked list.
from link_list_utils import LinkNode, LinkList
class Solution:
    def partition(self, head: LinkNode, x: int) -> LinkNode:
        more_dummy = LinkNode(-1)
        more_pointer = more_dummy
        less_dummy = LinkNode(-2)
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

            # print for test
            print(pointer is not None)
            # print("more_dummy", LinkList.show_from_node(more_dummy))
            # print("less_dummy", LinkList.show_from_node(less_dummy))
            # print("pointer", LinkList.show_from_node(pointer))
            # print("head", LinkList.show_from_node(head))
            print("************************")
            print()

        less_pointer.next = more_dummy.next

        return less_dummy.next


if __name__ == "__main__":
    the_link = LinkList([1,4,3,2,5,2])
    the_int = 3
    the_s = Solution()
    the_new_link_head = the_s.partition(the_link.head, the_int)
    print(LinkList.show_from_node(the_new_link_head))