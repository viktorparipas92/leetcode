'''
150. Evaluate Reverse Polish Notation
------------------------------------------------
Difficulty: Medium

You are given an array of strings tokens that represents an arithmetic
expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the
expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish
  notation.
- The answer and all the intermediate calculations can be represented in a
  32-bit integer.
'''
import operator

ADDITION = '+'
MULTIPLICATION = '*'
SUBTRACTION = '-'
DIVISION = '/'

class Solution:
    operators = {ADDITION, MULTIPLICATION, SUBTRACTION, DIVISION}

    def __init__(self):
        self.stack = []

    def is_operator(self, token):
        return token in self.operators

    def evaluate(self, token, *operands):
        if token == ADDITION:
            return sum(operands)
        elif token == SUBTRACTION:
            return operator.sub(*operands)
        elif token == MULTIPLICATION:
            return operator.mul(*operands)
        elif token == DIVISION:
            return int(operator.truediv(*operands))

    def evaluate_reverse_polish_notation(self, tokens: list[str]) -> int:
        self.stack = []
        for token in tokens:
            if self.is_operator(token):
                last = self.stack.pop()
                second_to_last = self.stack.pop()
                
                result = self.evaluate(token, second_to_last, last)
                self.stack.append(int(result))
            else:
                self.stack.append(int(token))

        return self.stack[0]
    

def test_evaluate_reverse_polish_notation():
    solution = Solution()
    inputs = [
        ['2', '1', '+', '3', '*'],
        ['4', '13', '5', '/', '+'],
        ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']
    ]
    outputs = [9, 6, 22]
    for input, output in zip(inputs, outputs):
        assert solution.evaluate_reverse_polish_notation(input) == output


if __name__ == '__main__':
    test_evaluate_reverse_polish_notation()
    