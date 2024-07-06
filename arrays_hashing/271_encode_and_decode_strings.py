"""
271. Encode and Decode Strings
-----------------------------------
Difficulty: Medium

Design an algorithm to encode a list of strings to a string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
"""

class Solution:
    def encode(self, strings: list[str]) -> str:
        return ''.join(f'{len(s)}:{s}' for s in strings)

    def decode(self, string: str) -> list[str]:
        strings = []
        i = 0
        while i < len(string):
            j = string.find(':', i)
            i = j + 1 + int(string[i:j])
            strings.append(string[j + 1:i])

        return strings


def test_encode_decode():
    solution = Solution()
    strings = ['hello', 'world']
    encoded = solution.encode(strings)
    assert solution.decode(encoded) == strings

    strings = ['', 'hello', '', 'world']
    encoded = solution.encode(strings)
    assert solution.decode(encoded) == strings

    strings = []
    encoded = solution.encode(strings)
    assert solution.decode(encoded) == strings

    strings = ['hello', 'world', '']
    encoded = solution.encode(strings)
    assert solution.decode(encoded) == strings


if __name__ == '__main__':
    test_encode_decode()
