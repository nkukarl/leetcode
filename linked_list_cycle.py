class Solution(object):
    def has_cycle(self, head):
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def detect_cycle(self, head):
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                ss = head
                ff = fast
                while ss != ff:
                    ss = ss.next
                    ff = ff.next
                return ss
        return None
