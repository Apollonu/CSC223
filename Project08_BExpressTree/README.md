# Binary Expression Tree - Project 08

A binary expression tree that is built with a postfix expression,
uses a stack of partial trees and evaluates them recursively and
will output the postfix and infix forms.

Supports operands for ints, decimals, and negatives
Supports binary operators + - * /
The operands are stored in a leaf and each operator in a node
The first subtree popped in construction is the Right child, the second is the Left child

Invalid expressions will raise ValueError (empty, bad token, few operands, too many operands) or ZeroDivisionError (Division By Zero)

## Files
- `stack.py` - Stack reused from previous project
- `binary_expression_tree.py` - Includes the Node and BinaryExpressionTree classes
- `main.py` - Driver that imports BinaryExpressionTree and handles valid, invalid, and traversal cases
- `test_binary_expression_tree.py` - Unittest suite for BinaryExpressionTree

## Running
    python binary_expression_tree.py
    python main.py
    python -m unittest test_binary_expression_tree.py -v
