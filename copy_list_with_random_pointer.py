class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copy_random_list(self, head):
        # Handle simple scenario
        if head is None:
            return None
        # Take the following list as an example
        # # # # # # # # # # # # # # # # #
        #                               #
        #    . . . . . . . . . . . .    #
        #    .         . .         .    #
        #    v         . v         .    #
        #   [1]------->[2]------->[3]   #
        #    .                     ^    #
        #    .                     .    #
        #    . . . . . . . . . . . .    #
        #                               #
        # # # # # # # # # # # # # # # # #
        node = head
        while node is not None:
            next_ = node.next
            node.next = RandomListNode(node.label)
            node.next.next = next_
            node = next_
        # # # # # # # # # # # # # # # # # # # # # # #
        #                                           #
        #    . . . . . . . . . . . . . .            #
        #    .           . .           .            #
        #    v           . v           .            #
        #   [1]-->[1']-->[2]-->[2']-->[3]-->[3']    #
        #    .                         ^            #
        #    .                         .            #
        #    . . . . . . . . . . . . . .            #
        #                                           #
        # # # # # # # # # # # # # # # # # # # # # # #
        node = head
        while node is not None:
            if node.random is not None:
                node.next.random = node.random.next
            else:
                node.next.random = None
            node = node.next.next
        # # # # # # # # # # # # # # # # # # # # # # #
        #                                           #
        #    . . . . . . . . . . . . . .            #
        #    .           . .           .            #
        #    .     * * * o o * * * * * o * * *      #
        #    .     *     . .   * *     .     *      #
        #    v     v     . v   * v     .     *      #
        #   [1]-->[1']-->[2]-->[2']-->[3]-->[3']    #
        #    .     *                   ^     ^      #
        #    .     *                   .     *      #
        #    .     * * * * * * * * * * o * * *      #
        #    .                         .            #
        #    . . . . . . . . . . . . . .            #
        #                                           #
        # # # # # # # # # # # # # # # # # # # # # # #
        head_ = head.next
        node = head
        node_ = head_
        cur = head.next.next
        while cur is not None:
            node.next = cur
            node = node.next
            node_.next = cur.next
            node_ = node_.next
            cur = cur.next.next
        node.next = None
        # # # # # # # # # # # # # # # # #
        #                               #
        #    . . . . . . . . . . . .    #
        #    .         . .         .    #
        #    v         . v         .    #
        #   [1]------->[2]------->[3]   #
        #    .                     ^    #
        #    .                     .    #
        #    . . . . . . . . . . . .    #
        #                               #
        #    * * * * * * * * * * * *    #
        #    *         * *         *    #
        #    v         * v         *    #
        #   [1']------>[2']----->[3']   #
        #    *                     ^    #
        #    *                     *    #
        #    * * * * * * * * * * * *    #
        #                               #
        # # # # # # # # # # # # # # # # #

        return head_
