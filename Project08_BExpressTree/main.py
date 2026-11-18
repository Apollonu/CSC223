from binary_expression_tree import BinaryExpressionTree

def main():
    '''
        Driver for Project08_BExpresstree
        Shows postfix input, infix, and the generated result including the postfix
        Reports errors without halting tests
    '''
    print("------ Expression Trees ------")
    for express in  [
        "2 4 6 * +",
        "6 2 / 4 -",
        "2 2 / 6 +",
        "6 4 + 10 *",
        "-4 2.2 *",
        "6 4 2 * * 2 /",
        "30 2 4 * -",
        "4 -",
        "8 6 4 /",
        "6 4 ? *",
        "7 0 /",
        ""
    ]:
        try:
            tree = BinaryExpressionTree(express)
            print(
                f"[{express}] infix: {tree.infix()} "
                f"postfix: {tree.postfix()} = {tree.eval()}"
            )
        except (ValueError, ZeroDivisionError) as error:
            print(f"[{express}] -> ERROR: {error}")

    print("------ Traversals ------")
    for express in [
        "2 4 6 * +",
        "6 2 / 4 -"
    ]:
        tree = BinaryExpressionTree(express)
        print(
            f"[{express}]"
            f"  preorder: {' '.join(tree.preorder())}"
            f"  inorder: {' '.join(tree.inorder())} (no parentheses)"
            f"  postorder: {' '.join(tree.postorder())}"
        )

if __name__ == "__main__":
    main()
