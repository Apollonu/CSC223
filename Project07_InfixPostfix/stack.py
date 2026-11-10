class Stack:
    '''
        A stack class that sorts items in LIFO order
        Clients will interact with this as a public interface
        peek and pop return IndexError if empty
    '''
    def __init__(self):
        '''Creates an empty stack'''
        self._items = []

    def push(self, item):
        '''Pushes an item to the top of the stack'''
        self._items.append(item)

    def pop(self):
        '''Removes and then returns the top item of the stack'''
        if self.is_empty():
            raise IndexError("pop from Stack")
        return self._items.pop()

    def peek(self):
        '''Returns the top item without removing it from the stack'''
        if self.is_empty():
            raise IndexError("peek at Stack")
        return self._items[-1]

    def is_empty(self):
        '''Returns true if the stack has no items, otherwise return false'''
        return len(self._items) == 0

    def size(self):
        '''Returns the number of items in the stack'''
        return len(self._items)

if __name__ == "__main__":
    Stack = Stack()

    for oper in (Stack.pop, Stack.peek):
        try:
            oper()
            print(f"FAIL: {oper.__name__} on empty Stack")
        except IndexError:
            print(f"PASS: {oper.__name__} on empty Stack raises IndexError")

    Stack.push(1)
    assert Stack.size() == 1, "size after push"
    Stack.push(2); Stack.push(3)
    assert Stack.peek() == 3 and Stack.size() == 3, "peek should not remove"
    assert [Stack.pop(), Stack.pop(), Stack.pop()] == [3, 2, 1], "pop reverses order"
    assert Stack.is_empty(), "Stack empty after removal"

    print("All Stack tests finished")
