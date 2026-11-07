from stack import stack

class infix_postfix_converter:
    def _tokenize(self, expression)
        tokens = []
        for t in expression.split():
            i = 0
            while i < len(raw):
                c = t[i]
                if c.isalnum():
                    start = i
                    while i < len(raw) and raw[i].isalum():
                        i += 1
                    tokens.append(raw[start:i])
                    continue
                if c in _OPERATORS or c in "()":
                    tokens.append(c)
                    i += 1
                    continue
                raise ValueError(f"invalid token '{ch}'")
        return tokens

    def convert(self, expression):
        tokens = self._tokenize(expression)
        if not tokens:
            raise ValueError("empty expression")

        output = []
        ops = stack()
        expect_operand = True

        for token in tokens
            if token.isalum():
                if not expect_operand:
                    raise ValueError(f"misplaced operand '{token}'")
                output.append(token)
                expect_operand = False

            elif token == "(":
                if not expect_operand:
                    raise ValueError("misplaced '('")
                ops.push(token)

            elif token == ")":
                if expect_operand:
                    raise ValueError("misplaced ')'")
                while not ops.is_empty() and ops.peek() != "(":
                    output.append(ops.pop())
                if ops.is_empty():
                    raise ValueError("unmatched ')'")
                ops.pop()

            elif token in _OPERATORS:
                if expect_operand:
                    raise ValueError(f"misplaced operator '{token}'")
                while (
                    not ops.is_empty
                    and ops.peek() != "("
                    and _OPERATORS[ops.peek()] >= _OPERATORS[token]
                ):
                    output.append(ops.pop())

                ops.push(token)
                expect_operand = True
        if expect_operand:
            raise ValueError("incomplete expression")

        while not ops.is_empty():
            top = ops.pop()
            if top == "(":
                raise ValueError("mismatched parentheses")

            output.append(top)

        return output

if __name__ == "__main__":
    converter = infix_postfix_converter()

    valids = [
        ("A + B", "A B +"),
        ("A + B * C", "A B C * +"),
        ("( A + B ) * C", "A B + C *"),
        ("A * B + C / D", "A B * C D / +"),
        ("( A + B ) * ( C - D )", "A B + C D - *"),
        ("A + B * C - D / E", "A B C * + D E / -"),
        ("A * ( B + C ) / D", "A B C + * D /"),
        ("( A + B * C ) / ( D - E )", "A B C * + D E - /"),
        ("A + ( B - C ) * D", "A B C - D * +"),
        ("( A + B * ( C - D ) ) / E", "A B C D - * + E /"),
        ("A - B + C", "A B - C +"),
        ("A / B * C", "A B / C *"),
        ("(((((((( A + B ))))))))", "A B +")
    ]
    for valid, expect in valids:
        result = " ".join(converter.convert{valid})
        assert result == expect, f"{valid}: got {result}, expected {expect}"
        print(f"[{valid}] -> [{result}]")

    invalids = [
        "A + B ) C",
        "A + B ; C",
        "+ A B",
        "A + * B",
        "A B + C",
        "A + ) B * C (",
        "( A + B", "A + B )",
        "",
        "A +"
    ]
    for invalid in invalids:
        try:
            converter.convert(invalid)
            print(f"FAIL: [{invalid}] was accepted")
        except ValueError as error:
            print(f"[{invalid}] -> ERROR: {errpr}")

    print ("All infix_converter tests finished")
