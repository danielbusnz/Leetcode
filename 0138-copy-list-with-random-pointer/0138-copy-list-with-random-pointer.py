
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        # Step 1: Create copies of every node
        current = head

        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Step 2: Connect the copied nodes
        current = head

        while current:
            copy = old_to_new[current]

            copy.next = old_to_new.get(current.next)
            copy.random = old_to_new.get(current.random)

            current = current.next

        # Step 3: Return the head of the copied list
        return old_to_new[head]
