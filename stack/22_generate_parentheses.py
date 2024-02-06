'''
22. Generate Parentheses
----------------------------------
Difficulty: Medium

Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.
'''


class Solution:
    def __init__(self):
        self.result = []
        self.stack = []

    def generate_parentheses(self, n: int) -> list[str]:
        self.backtrack(n, num_open=0, num_closed=0)
        return self.result

    def backtrack(self, n, num_open: int, num_closed: int):
        if len(self.stack) == 2 * n:
            self.result.append(''.join(self.stack))
            return

        if num_open < n:
            self.stack.append('(')
            self.backtrack(n, num_open + 1, num_closed)
            self.stack.pop()

        if num_closed < num_open:
            self.stack.append(')')
            self.backtrack(n, num_open, num_closed + 1)
            self.stack.pop()

    def reset(self):
        self.result = []
        self.stack = []


def test_generate_parentheses():
    solution = Solution()
    assert solution.generate_parentheses(3) == [
        '((()))', '(()())', '(())()', '()(())', '()()()'
    ]

    solution.reset()
    assert solution.generate_parentheses(1) == ['()']


if __name__ == '__main__':
    test_generate_parentheses()