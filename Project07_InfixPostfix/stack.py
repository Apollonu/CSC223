class stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from stack")
        return self._item.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

if __name__ == "__main__":
    stack = stack()
