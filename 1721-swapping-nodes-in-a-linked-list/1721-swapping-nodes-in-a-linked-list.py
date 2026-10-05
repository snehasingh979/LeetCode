class Solution:
    def swapNodes(self, head, k):
        # Find kth node from beginning
        first = head

        for _ in range(k - 1):
            first = first.next

        # Find kth node from end
        second = head
        temp = first

        while temp.next:
            temp = temp.next
            second = second.next

        # Swap values
        first.val, second.val = second.val, first.val

        return head
        