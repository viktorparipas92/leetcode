"""
127. Word Ladder
----------------
Difficulty: Hard

You are given two words, beginWord and endWord, and also a list of words wordList.
All the given words are of the same length, consisting of lowercase English letters,
and are all distinct.

Your goal is to transform beginWord into endWord by following the rules:
- You may transform beginWord to any word within wordList,
  provided that at exactly one position the words have a different character,
  and the rest of the positions have the same characters.
- You may repeat the previous step with the new word that you obtain,
  and you may do this as many times as needed.

Return the minimum number of words within the transformation sequence
needed to obtain the endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]
Output: 4
Explanation: The transformation sequence is "cat" -> "bat" -> "bag" -> "sag".

Example 2:
Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sat","dag","dot"]
Output: 0
Explanation: There is no possible transformation sequence from "cat" to "sag" since the word "sag" is not in the wordList.

Constraints:
1 <= beginWord.length <= 10
1 <= wordList.length <= 100
"""
import string
from collections import deque


def ladder_length_breadth_first_search(begin_word: str, end_word: str, word_list: list[str]) -> int:
    """
    Time complexity: O(N * L^2)
    Space complexity: O(N * L)
    where N is the number of words in word_list and L is the length of each word.
    """
    if (end_word not in word_list) or (begin_word == end_word):
        return 0

    words: set = set(word_list)
    result: int = 0
    word_queue = deque([begin_word])
    while word_queue:
        result += 1
        for _ in range(len(word_queue)):
            left_word = word_queue.popleft()
            if left_word == end_word:
                return result

            for i in range(len(left_word)):
                for char in string.ascii_lowercase:
                    if char == left_word[i]:
                        continue

                    neighbour: str = left_word[:i] + char + left_word[i + 1:]
                    if neighbour in words:
                        word_queue.append(neighbour)
                        words.remove(neighbour)

    return 0


def ladder_length_meet_in_the_middle_bfs(
    begin_word: str,
    end_word: str,
    word_list: list[str],
) -> int:
    if end_word not in word_list or begin_word == end_word:
        return 0

    word_length: int = len(word_list[0])

    words: set[str] = set(word_list)

    queue_beginning = deque([begin_word])
    from_beginning: dict[str, int] = {begin_word: 1}

    queue_end = deque([end_word])
    from_end: dict[str, int] = {end_word: 1}

    while queue_beginning and queue_end:
        if len(queue_beginning) > len(queue_end):
            queue_beginning, queue_end = queue_end, queue_beginning  # Swap to always expand the smaller queue
            from_beginning, from_end = from_end, from_beginning

        for _ in range(len(queue_beginning)):
            left_word = queue_beginning.popleft()
            num_steps: int = from_beginning[left_word]
            for i in range(word_length):
                for char in string.ascii_lowercase:
                    if char == left_word[i]:
                        continue

                    neighbour: str = left_word[:i] + char + left_word[i + 1:]
                    if neighbour not in words:
                        continue
                    elif neighbour in from_end:
                        return num_steps + from_end[neighbour]
                    elif neighbour not in from_beginning:
                        from_beginning[neighbour] = num_steps + 1
                        queue_beginning.append(neighbour)

    return 0


def test_ladder_length():
    solutions = [
        ladder_length_breadth_first_search,
        ladder_length_meet_in_the_middle_bfs,
    ]

    test_cases = [
        ('cat', 'sag', ['bat', 'bag', 'sag', 'dag', 'dot'], 4),
        ('cat', 'sag', ['bat', 'bag', 'sat', 'dag', 'dot'], 0),
    ]

    for solution in solutions:
        for begin_word, end_word, word_list, expected_ladder_length in test_cases:
            # Act
            ladder_length = solution(begin_word, end_word, word_list)

            # Assert
            assert ladder_length == expected_ladder_length

        print(f'{solution.__name__} passed all tests!')


if __name__ == '__main__':
    test_ladder_length()
    print('All tests passed!')
