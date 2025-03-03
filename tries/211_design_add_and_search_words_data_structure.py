"""
211. Design Add and Search Words Data Structure
-------------------------------------------------
Difficulty: Medium

Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:
- void addWord(word) Adds word to the data structure.
- bool search(word) Returns true if there is any string in the data structure that
  matches word or false otherwise. word may contain dots '.' where dots can be
  matched with any letter.

Example 1:
Input:
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search",
"say", "search", "day", "search", ".ay", "search", "b.."]
Output:
[null, null, null, null, false, true, true, true]
Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true

Constraints:
1 <= word.length <= 20
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
"""


class WordDictionaryBruteForce:
    """
    Time complexity: O(1) for add_word(), O(m*n) for search().
    Space complexity: O(m*n)
    """
    def __init__(self):
        self.store: list = []

    def add_word(self, word: str) -> None:
        self.store.append(word)

    def search(self, word: str) -> bool:
        for stored_word in self.store:
            if len(stored_word) != len(word):
                continue

            is_matching = all(
                stored_char == char or char == '.'
                for stored_char, char in zip(stored_word, word)
            )
            if is_matching:
                return True

        return False

class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_word_found: bool = False


class WordDictionaryTrie:
    """
    Time complexity: O(n) for add_word(), O(n) for search().
    Space complexity: O(t + n)
    """
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        current_node = self.root
        for char in word:
            current_node = current_node.children.setdefault(char, TrieNode())

        current_node.is_word_found = True

    def search(self, word: str) -> bool:
        def depth_first_search(j, root_node: TrieNode):
            current_node = root_node

            for i, char in enumerate(word[j:], start=j):
                if char == '.':
                    return any(
                        depth_first_search(i + 1, child_node)
                        for child_node in current_node.children.values()
                    )
                elif char not in current_node.children:
                    return False
                else:
                    current_node = current_node.children[char]

            return current_node.is_word_found

        return depth_first_search(j=0, root_node=self.root)


def test_word_dictionary():
    solutions = [
        WordDictionaryBruteForce,
        WordDictionaryTrie,
    ]

    for solution in solutions:
        # Act
        word_dictionary = solution()
        word_dictionary.add_word('day')
        word_dictionary.add_word('bay')
        word_dictionary.add_word('may')

        # Assert
        assert not word_dictionary.search('say')
        assert word_dictionary.search('day')
        assert word_dictionary.search('.ay')
        assert word_dictionary.search('b..')

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_word_dictionary()

