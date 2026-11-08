from infix_converter import infix_postfix_converter
from postfix_evaluator import postfix_evaluator

def main():
    postfix_cases = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "26 28 + 32 2 ; - 5 /",
        "2 3 4 +",
        "8 0 /"
    ]
    for expression in postfix_cases:
        try:
            result = postfix_evaluator().evaluate(expression)
            print(f"[{expression}] = {result}")
        except (ValueError, ZeroDivisionError) as error:
            print(f"[{expression}] -> ERROR: {error}")

    infix_cases = [
        "A + B",
        "A + B * C",
        "( A + B ) * C",
        "A + * B",
        "( A + B",
        "A + B ; C",
        "A B + C"
    ]
    converter = infix_postfix_converter()
    for expression in infix_cases:
        try:
            result = " ".join(converter.convert(expression))
            print(f"[{expression}] = {result}")
        except (ValueError, ZeroDivisionError) as error:
            print(f"[{expression}] -> ERROR: {error}")

    pipeline_cases = [
        "3 + 4 * 2",
        "( 10 - 4 ) / 3",
        "7 * ( 2 + 5 )",
        "9 / ( 4 - 4 )"
    ]
    for expression in pipeline_cases:
        try:
            token = converter.convert(expression)
            result = postfix_evaluator().evaluate(" ".join(token))
            postfix = " ".join(token)
            print(f"[{expression}] -> [{postfix}] = {result}")
        except (ValueError, ZeroDivisionError) as error:
            print(f"[{expression}] -> ERROR: {error}")

if __name__ == "__main__":
    main()
