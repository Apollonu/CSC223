from stack import stack

_OPERATORS = {"+", "-", "*", "/"}

class postfix_evaluator:
    def evaluate(self, expression):
        tokens = expression.split()

        if not tokens:
            raise ValueError("empty expression")

        operand = stack()
