# leetcode training
# https://leetcode.cn/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1_head: ListNode, list2_head: ListNode) -> ListNode:
        dummy = ListNode(-1)  # dummy 节点作为合并后链表的起点 (有序，升序链表）
        pointer = dummy  # 合并链表的指针初始化为 dummy
        list1_pointer = list1_head  # 链表1的指针指向链表1的头节点
        list2_pointer = list2_head  # 链表2的指针指向链表2的头节点
        while list1_pointer and list2_pointer:  # 当此时两个指针都指向各自链表的有效元素时，进行循环
            # 此循环判断条件可确保链表1和链表2之中必定有一个链表已经全部合并到合并链表中了
            if list1_pointer.val > list2_pointer.val:  # 当链表1的元素大于链表2的元素时
                pointer.next = list2_pointer  # 合并链表的指针指向链表2的当前元素（值较小的元素）
                list2_pointer = list2_pointer.next  # 链表2的指针指向链表2的下一个元素
            else:  # 当链表1的元素小于链表2的元素时
                pointer.next = list1_pointer  # 合并链表的指针指向链表1的元素
                list1_pointer = list1_pointer.next  # 链表1的指针指向链表1的下一个元素
            pointer = pointer.next  # 合并链表的指针指向此合并链表新加入的元素（链表1或链表2中较小的元素）

        # 链表1和链表2元素比较的循环结束之后，分别判断链表1和链表2是否还有元素
        if list1_pointer:  # 如果链表1中还存有元素未加入合并链表
            pointer.next = list1_pointer  # 合并链表的指针指向当前链表1的指针，即将链表1的剩余元素连接都合并链表中（链表1本身已是有序）

        if list2_pointer:  # 如果链表2中还存有元素未加入合并链表
            pointer.next = list2_pointer  # 合并链表的指针指向当前链表2的指针，即将链表2的剩余元素连接都合并链表中（链表2本身已是有序）

        return dummy.next  # 最后返回 dummy 的下一次元素，即合并链表的头节点


if __name__ == '__main__':
    pass
