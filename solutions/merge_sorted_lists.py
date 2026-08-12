# Merge Two Sorted Lists
# Combina dos listas enlazadas ordenadas en una sola lista ordenada.
#
# Fecha: 2026-08-12

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


if __name__ == '__main__':
    # 1->2->4  +  1->3->4  =>  1->1->2->3->4->4
    a = ListNode(1, ListNode(2, ListNode(4)))
    b = ListNode(1, ListNode(3, ListNode(4)))
    node = merge_two_lists(a, b)
    while node:
        print(node.val, end=' ')
        node = node.next
