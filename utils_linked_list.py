class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def get_head_linked_list(linked_list_raw):
    """

    Args:
        linked_list_raw (list):

    Returns:
        ListNode

    """
    dummy = ListNode(0)
    node = dummy
    for val in linked_list_raw:
        node.next = ListNode(val)
        node = node.next
    return dummy.next


def retrieve_tail_linked_list(head):
    """

    Args:
        head (ListNode):

    Returns:
        ListNode

    """
    node = head
    while node.next is not None:
        node = node.next
    return node


def compare_linked_lists(head1, head2):
    """

    Args:
        head1 (ListNode): head of linked list
        head2 (ListNode): head of linked list

    Returns:
        bool

    """
    if head1 is None and head2 is None:
        return True
    node1, node2 = head1, head2
    while node1 is not None and node2 is not None:
        if node1.val != node2.val:
            return False
        node1 = node1.next
        node2 = node2.next
    if node1 is not None or node2 is not None:
        return False
    return True
