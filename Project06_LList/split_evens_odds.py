from singly_linked_list import SinglyLinkedList

class SplitEvensOdds(SinglyLinkedList):
    def split_even_odd(self):
        if self._count == 0:
            raise ValueError("split_even_odd failed: the list is empty.")

        evens = SplitEvensOdds()
        odds = SplitEvensOdds()

        current = self._head
        while current is not None:
            following = current.next
            current.next = None

            if current.data % 2 == 0:
                target = evens
            else:
                target = odds

            if target._tail is None:
                target._head = current
            else:
                target._tail.next = current
            target._tail = current
            target._count += 1

            current = following

        self._head = None
        self._tail = None
        self._count = 0

        return evens, odds
