"""
108. Implement Trie (Prefix Tree)
---------------------------------
Difficulty: Medium

A prefix tree (also known as a trie) is a tree data structure used to efficiently store 
and retrieve keys in a set of strings. 
Some applications of this data structure include auto-complete and spellchecker systems.

Implement the PrefixTree class:
- PrefixTree() Initializes the prefix tree object.
- void insert(String word) Inserts the string word into the prefix tree.
- boolean search(String word) Returns true if the string word is in the prefix tree 
  (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted 
  string word that has the prefix `prefix`, and false otherwise.
  
Example 1:
Input: 
[
    'Trie', 'insert', 'dog', 'search', 'dog', 'search', 'do', 'startsWith', 'do', 
    'insert', 'do', 'search', 'do'
]
Output:
[null, null, true, false, true, null, true]

Explanation:
PrefixTree prefixTree = new PrefixTree();
prefixTree.insert('dog');
prefixTree.search('dog');    // return true
prefixTree.search('do');     // return false
prefixTree.startsWith('do'); // return true
prefixTree.insert('do');
prefixTree.search('do');     // return true

Constraints:
1 <= word.length, prefix.length <= 1000
word and prefix are made up of lowercase English letters.
"""


class TrieNode:
    def __init__(self):
        self.end_of_word = False


class PrefixTree:
    NODE_CLASS = TrieNode

    def __init__(self):
        self.root = self.NODE_CLASS()

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def starts_with(self, prefix: str) -> bool:
        raise NotImplementedError


class TrieNodeWithArray(TrieNode):
    def __init__(self):
        super().__init__()
        self.children: list[TrieNode | None] = [None] * 26


class PrefixTreeWithArray(PrefixTree):
    """
    Time complexity: O(n) for all operations, where n is the length of the word
    Space complexity: O(t) for all operations, where t is the total number of nodes
    """
    NODE_CLASS = TrieNodeWithArray

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            i = self.get_index(char)
            if current_node.children[i] is None:
                current_node.children[i] = self.NODE_CLASS()

            current_node = current_node.children[i]

        current_node.end_of_word = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            i = self.get_index(char)
            if current_node.children[i] is None:
                return False

            current_node = current_node.children[i]

        return current_node.end_of_word

    def starts_with(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            i = self.get_index(char)
            if current_node.children[i] is None:
                return False

            current_node = current_node.children[i]

        return True

    @staticmethod
    def get_index(char: str) -> int:
        return ord(char) - ord('a')


class TrieNodeWithHashMap(TrieNode):
    def __init__(self):
        super().__init__()
        self.children: dict[str, TrieNode] = {}


class PrefixTreeWithHashMap(PrefixTree):
    """
    Time complexity: O(n) for all operations, where n is the length of the word
    Space complexity: O(t) for all operations, where t is the total number of nodes
    """
    NODE_CLASS = TrieNodeWithHashMap

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = self.NODE_CLASS()

            current_node = current_node.children[char]

        current_node.end_of_word = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.end_of_word

    def starts_with(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return True


def test_prefix_tree() -> None:
    solutions = [
        PrefixTreeWithArray,
        PrefixTreeWithHashMap,
    ]

    for Trie in solutions:
        # Arrange
        prefix_tree = Trie()

        # Act, Assert
        prefix_tree.insert('dog')
        assert prefix_tree.search('dog') is True
        assert prefix_tree.search('do') is False
        assert prefix_tree.starts_with('do') is True

        prefix_tree.insert('do')
        assert prefix_tree.search('do') is True

        print(f'All tests passed for {Trie.__name__}!')


if __name__ == '__main__':
    test_prefix_tree()
