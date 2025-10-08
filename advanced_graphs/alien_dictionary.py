"""
Alien Dictionary
-----------------
Difficulty: Hard

There is a foreign language which uses the latin alphabet,
but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary,
where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language.
If the order is invalid, return an empty string.
If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:
- The first letter where they differ is smaller in a than in b.
- a is a prefix of b and a.length < b.length.

Example 1:
Input: ["z","o"]
Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:
Input: ["hrn","hrf","er","enn","rfnn"]
Output: "hernf"

Explanation:
from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know get 'r' < 'n'
from "enn" and "rfnn" we know 'e'<'r'
so one possibile solution is "hernf"

Constraints:
The input words will contain characters only from lowercase 'a' to 'z'.
1 <= words.length <= 100
1 <= words[i].length <= 100
"""


def foreign_dictionary_dfs(words: list[str]) -> str:
    """
    Time complexity: O(N + V + E)
    Space complexity: O(V + E)
    where N is the total length of all words in the input list,
    V is the number of unique characters in the input list,
    and E is the number of edges in the graph, i.e. the number of precedence relations.
    """
    def depth_first_search(character: str) -> bool:
        if character in is_visited_map:
            return is_visited_map[character]

        is_visited_map[character] = True
        for neighbour_char in adjacency_map[character]:
            if depth_first_search(neighbour_char):
                return True

        is_visited_map[character] = False
        alphabet.append(character)

    adjacency_map: dict[str, set] = {_char: set() for word in words for _char in word}
    for i in range(len(words) - 1):
        word_1 = words[i]
        word_2 = words[i + 1]
        min_length: int = min(len(word_1), len(word_2))
        if len(word_1) > len(word_2) and word_1[:min_length] == word_2[:min_length]:
            return ''

        for j in range(min_length):
            char_1 = word_1[j]
            char_2 = word_2[j]
            if char_1 != char_2:
                adjacency_map[char_1].add(char_2)
                break

    is_visited_map: dict[str, bool] = {}
    alphabet: list[str] = []
    for _character in adjacency_map:
        if depth_first_search(_character):
            return ''

    alphabet.reverse()
    return ''.join(alphabet)


def test_foreign_dictionary():
    solutions = [
        foreign_dictionary_dfs,
    ]

    test_cases = [
        (['z', 'o'], 'zo'),
        (['hrn', 'hrf', 'er', 'enn', 'rfnn'], 'hernf'),
    ]

    for solution in solutions:
        for words, expected_alphabet in test_cases:
            # Act
            alphabet = solution(words)

            # Assert
            assert alphabet == expected_alphabet

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_foreign_dictionary()