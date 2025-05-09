"""
43. Multiply Strings
--------------------
Difficulty: Medium

You are given two strings num1 and num2 that represent non-negative integers.
Return the product of num1 and num2 in the form of a string.
Assume that neither num1 nor num2 contain any leading zero,
unless they are the number 0 itself.
Note: You can not use any built-in library to convert the inputs directly into integers.

Example 1:
Input: num1 = "3", num2 = "4"
Output: "12"

Example 2:
Input: num1 = "111", num2 = "222"
Output: "24642"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
"""


def multiply_strings(number_1: str, number_2: str) -> str:
    """
    Time complexity: O(m * n)
    Space complexity: O(m + n)
    where m is the length of num1 and n is the length of num2.
    """
    if '0' in {number_1, number_2}:
        return '0'

    product = [0] * (len(number_1) + len(number_2))
    total_length = len(product)

    number_1, number_2 = number_1[::-1], number_2[::-1]  # Reverse the strings
    for index_1, char_1 in enumerate(number_1):
        for index_2, char_2 in enumerate(number_2):
            digit = int(char_1) * int(char_2)
            product[index_1 + index_2] += digit
            product[index_1 + index_2 + 1] += product[index_1 + index_2] // 10
            product[index_1 + index_2] = product[index_1 + index_2] % 10

    product = product[::-1]  # Reverse the product to get the correct order
    start_index = 0
    while start_index < total_length and product[start_index] == 0:
        start_index += 1

    product = map(str, product[start_index:])
    return ''.join(product)


def test_multiply_strings():
    solutions = [
        multiply_strings,
    ]

    test_cases = [
        (('3', '4'), '12'),
        (('111', '222'), '24642'),
    ]

    for solution in solutions:
        for (number_1, number_2), expected_product in test_cases:
            # Act
            product = solution(number_1, number_2)

            # Assert
            assert product == expected_product

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_multiply_strings()
