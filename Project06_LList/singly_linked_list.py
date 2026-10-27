from node import Node


class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def _find_node(self, value):
        current = self._head
        while current is not None:
            if current.data == value:
                return current
            current = current.next
        return None

    def append(self, value):
        new_node = Node(value)
        if self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._count += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node
        if self._tail is None:
            self._tail = new_node
        self._count += 1

    def insert_after(self, existing_value, new_value):
        node = self._find_node(existing_value)
        if node is None:
            raise ValueError(
                f"insert_after failed: {existing_value!r} is not in the list."
            )

        new_node = Node(new_value)
        new_node.next = node.next
        node.next = new_node

        if node is self._tail:
            self._tail = new_node
        self._count += 1

    def remove(self, value):
        previous = None
        current = self._head
        while current is not None and current.data != value:
            previous = current
            current = current.next

        if current is None:
            raise ValueError(f"remove failed: {value!r} is not in the list.")

        if previous is None:
            self._head = current.next
        else:
            previous.next = current.next

        if current is self._tail:
            self._tail = previous

        current.next = None
        self._count -= 1

    def contains(self, value):
        return self._find_node(value) is not None

    def is_empty(self):
        return self._count == 0


    def __len__(self):
        return self._count

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self):
        parts = []
        current = self._head
        while current is not None:
            parts.append(str(current.data))
            current = current.next
        parts.append("None")
        return "Head -> " + " -> ".join(parts)

    def __repr__(self):
        return f"SinglyLinkedList({list(self)!r})"

    def build_list_forward(self, values):
        for value in values:
            self.append(value)

    def build_list_backward(self, values):
        for value in values:
            self.prepend(value)

    def remove_all(self, value):
        removed = 0
        previous = None
        current = self._head

        while current is not None:
            if current.data == value:
                following = current.next

                if previous is None:
                    self._head = following
                else:
                    previous.next = following

                if current is self._tail:
                    self._tail = previous

                current.next = None
                self._count -= 1
                removed += 1
                current = following
            else:
                previous = current
                current = current.next

        return removed
