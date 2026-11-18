from stack import Stack

class Node:
    '''
        A node based linked binary expression tree
        Reads elements through element()
        Stores an element and links to its parent and child(ren)
    '''
    def __init__(self, element, parent=None):
        self._element = element
        self._parent = parent
        self._left = None
        self._right = None

    def element(self):
        '''Returns stored element'''
        return self._element

class BinaryExpressionTree:
    '''
        A linked binary expression tree that uses postfix expressions
        Stack is utilized from stack.py to combine partial trees
        Operators are internal nodes while the operands are the leaves
    '''
    _OPERATORS = {"+", "-", "*", "/"}

    def __init__(self, expression=None):
        '''Builds the tree or creates an empty one'''
        self._root = None
        self._size = 0
        if expression is not None:
            self._build(expression)

    def root(self):
        '''Returns the root position'''
        return self._root

    def left(self, p):
        '''Returns the left child position'''
        return p._left

    def right(self, p):
        '''Returns the right child position'''
        return p._right

    def parent(self, p):
        '''Returns the parent position'''
        return p._parent

    def leaf(self, p):
        '''Returns True if no children are found'''
        return p._left is None and p._right is None

    def size(self):
        '''Returns number of nodes in the tree'''
        return self._size

    def _is_number(self, token):
        '''Returns True if the token can be read as a number'''
        try:
            float(token)
            return True
        except ValueError:
            return False

    def subtrees(self, left_tree, right_tree):
        '''
            Attaches two trees into the utilized trees root
            Moves the nodes so that each node belongs to one tree
            This is done so that the source trees are emptied
            Results in zero copies or sharing
        '''
        if self._root is None:
            raise ValueError("root not found")
        if self._root._left is not None or self._root._right is not None:
            raise ValueError("root already found")

        self._attach(self._root, left_tree, True)
        self._attach(self._root, right_tree, False)

    def _attach(self, p, src_tree, src_left):
        '''Moves the root of the tree under p and empties it'''
        item = src_tree.root()
        item._parent = p
        if src_left:
            p._left = item
        else:
            p._right = item

        self._size += src_tree.size()
        src_tree._root = None
        src_tree._size = 0

    def _build(self, expr):
        '''
            Builds the tree from tokens
            First tree is the popped right operand and second is the left
            Raises ValueError for an empty input, bad token, or incorrect operand count
        '''
        def make_tree(element):
            tree = BinaryExpressionTree()
            tree._root = Node(element, None)
            tree._size = 1
            return tree

        tokens = expr.split()
        if not tokens:
            raise ValueError("expression found empty")

        partial = Stack()
        for token in tokens:
            if token in self._OPERATORS:
                if partial.size() < 2:
                    raise ValueError(f"too few operands for '{token}'")
                right_tree = partial.pop()
                left_tree = partial.pop()

                tree = make_tree(token)
                tree.subtrees(left_tree, right_tree)

                partial.push(tree)
            elif self._is_number(token):
                partial.push(make_tree(token))
            else:
                raise ValueError(f"unsupported token '{token}'")

        if partial.size() != 1:
            raise ValueError("too many operands")
        complete = partial.pop()
        self._root = complete._root
        self._size = complete._size

    def evaluate(self):
        '''Raises ZeroDivisionError for / 0 and evaluates expression tree'''
        if self._root is None:
            raise ValueError("no expression tree found")
        return self._evaluate_at(self._root)

    def _evaluate_at(self, p):
        '''Evaluates subtree at p'''
        if self.leaf(p):
            return float(p.element())
        left_val = self._evaluate_at(self.left(p))
        right_val = self._evaluate_at(self.right(p))
        op = p.element()
        if op == "+":
            return left_val + right_val
        if op == "-":
            return left_val - right_val
        if op == "*":
            return left_val * right_val
        if right_val == 0:
            raise ZeroDivisionError("division by zero")
        return left_val / right_val

    def infix(self):
        '''Returns parenthesized infix expression and () are added at every operator'''
        if self._root is None:
            raise ValueError("no expr tree")
        return self._infix(self._root)

    def _infix(self, p):
        '''Formats the subtree at p and () are added at each operator'''
        if self.leaf(p):
            return p.element()

        left_p = self._infix(self.left(p))
        right_p = self._infix(self.right(p))
        return f"({left_p} {p.element()} {right_p})"

    def postfix(self):
        '''Returns postfix expression in left right order, regenerates input tokens'''
        if self._root is None:
            raise ValueError("no expr tree")
        return " ".join(self.postorder())

    def preorder(self):
        '''Yields in root left right order'''
        yield from self._preorder(self._root)

    def _preorder(self, p):
        if p is not None:
            yield p.element()
            yield from self._preorder(p._left)
            yield from self._preorder(p._right)

    def inorder(self):
        '''Yields in left root right order, does not add ()'''
        yield from self._inorder(self._root)

    def _inorder(self, p):
        if p is not None:
            yield from self._inorder(p._left)
            yield p.element()
            yield from self._inorder(p._right)

    def postorder(self):
        '''Yields in left right root order'''
        yield from self._postorder(self._root)

    def _postorder(self, p):
        if p is not None:
            yield from self._postorder(p._left)
            yield from self._postorder(p._right)
            yield p.element()

if __name__ == "__main__":
    tree = BinaryExpressionTree("2 4 6 * +")

    assert tree.infix() == "(2 + (4 * 6))", tree.infix()
    assert tree.postfix() == "2 4 6 * +", tree.postfix()
    assert tree.evaluate() == 26.0, tree.evaluate()
    print("[2 4 6 * +]", tree.infix(), "=", tree.evaluate())

    check = BinaryExpressionTree("6 2 / 4 -")
    assert check.evaluate() == -1.0, check.evaluate()
    print("[6 2 / 4 -]", check.infix(), "=", check.evaluate())

    invalids = ["", "4 +", "4 6", "4 6 ? +"]
    for invalid in invalids:
        try:
            BinaryExpressionTree(invalid)
            print(f"FAIL: [{invalid}] was accepted")
        except (ValueError, ZeroDivisionError) as error:
            print(f"[{invalid}] -> ERROR: {error}")
    print("BinaryExpressionTree tests finished")
