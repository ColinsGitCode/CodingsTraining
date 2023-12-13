class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self, origin_list: list):
        self.head = LinkNode(origin_list[0])
        the_pointer = self.head
        for i in range(1, len(origin_list)):
            the_node = LinkNode(origin_list[i])
            the_pointer.next = the_node
            the_pointer = the_node

    def show_as_list(self):
        the_pointer = self.head
        the_element_list = []
        while the_pointer:
            the_element_list.append(the_pointer.val)
            the_pointer = the_pointer.next
        return the_element_list

    @staticmethod
    def show_from_node(head: LinkNode):
        the_pointer = head
        the_element_list = []
        while the_pointer:
            the_element_list.append(the_pointer.val)
            the_pointer = the_pointer.next
        return the_element_list



if __name__ == '__main__':
    the_list = [1, 2, 3, 4, 5]
    link_list = LinkList(the_list)
    print(link_list.show_as_list())
    print(link_list.head.val)
    print(link_list.head.next.val)
    print(link_list.head.next.next.val)
    print(link_list.head.next.next.next.val)
    print(link_list.head.next.next.next.next.val)
    print(link_list.head.next.next.next.next.next)
