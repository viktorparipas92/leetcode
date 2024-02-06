'''
22. Generate Parentheses
----------------------------------
Difficulty: Medium

Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.
'''


def generate_parentheses(n: int) -> list[str]:
    def backtrack(sequence: str, num_open: int, num_closed: int):
        if len(sequence) == 2 * n:
            result.append(sequence)
            return

        if num_open < n:
            backtrack(f'{sequence}(', num_open + 1, num_closed)

        if num_closed < num_open:
            backtrack(f'{sequence})', num_open, num_closed + 1)

    result = []
    backtrack('', num_open=0, num_closed=0)
    return result


def test_generate_parentheses():
    assert generate_parentheses(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']
    assert generate_parentheses(1) == ['()']


if __name__ == '__main__':
    test_generate_parentheses()