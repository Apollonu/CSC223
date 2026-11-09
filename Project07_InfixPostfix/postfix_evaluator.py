from stack import stack

_OPERATORS = {"+", "-", "*", "/"}

class postfix_evaluator:
    def evaluate(self, expression):
        tokens = expression.split()

        if not tokens:
            raise ValueError("empty expression")

        operand = stack()
        for token in tokens:
            if token in _OPERATORS:
                if operand.size() < 2:
                    raise ValueError(f"insuffient operands for operator '{token}'")
                right = operand.pop()
                left = operand.pop()
                if token == "+":
                    result = left + right
                elif token == "-":
                    result = left - right
                elif token == "*":
                    result = left * right
                else:
                    if right == 0:
                        raise ZeroDivisionError("divided by zero")
                    result = left / right
                operand.push(result)
            else:
                try:
                    operand.push(int(token))
                except ValueError:
                    try:
                        operand.push(float(token))
                    except ValueError:
                        raise ValueError(f"invalid token '{token}'")

        if operand.size() != 1:
            raise ValueError("operand size too big")
        return operand.pop()

if __name__ == "__main__":
    evaluator = postfix_evaluator()

    valids = [
        ("5 3 +", 8),
        ("8 2 - 3 +", 9),
        ("5 3 8 * +", 29),
        ("6 2 / 3 +", 6.0),
        ("5 8 + 3 -", 10),
        ("5 3 + 8 *", 64),
        ("8 2 3 * + 6 -", 8),
        ("5 3 8 * + 2 /", 14.5),
        ("8 2 + 3 6 * -", -8),
        ("5 3 + 8 2 / -", 4.0),
        ("35 27 + 3 *", 186),
        ("23 30 15 * /", 23 / (30 * 15)),
    ]
    for valid, expect in valids:
        result = evaluator.evaluate(valid)
        assert result == expect, f"{valid}: got {result}, expected {expect}"
        print(f"[{valid}] = {result}")

    invalids = [
        "26 28 + 32 2 ; - 5 /",
        "2 3 4 +", "20 29 9 * ;",
        "25 23 - +",
        "8 0 /",
        "5 +", "3 + 4", ""
    ]
    for invalid in invalids:
        try:
            evaluator.evaluate(invalid)
            print(f"FAIL: [{invalid}] was accepted")
        except (ValueError, ZeroDivisionError) as error:
            print(f"[{invalid}] -> ERROR: {error}")

    print("All postfix_evaluator tests finished")
