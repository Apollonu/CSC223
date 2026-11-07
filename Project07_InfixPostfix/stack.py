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

    for oper in (stack.pop, sstack.peek):          # error cases first (stack empty)
        try:
            op()
            print(f"FAIL: {oper.__name__} on empty stack")
        except IndexError:
            print(f"PASS: {oper.__name__} on empty stack raises IndexError")

    stack.push(1)
    assert stack.size() == 1, "size after push"
    stack.push(2); stack.push(3)
    assert stack.peek() == 3 and stack.size() == 3, "peek should not remove"
    assert [stack.pop(), stack.pop(), stack.pop()] == [3, 2, 1], "pop reverses order"
    assert stack.is_empty(), "stack empty after removal"

    print("All stack tests finished")
