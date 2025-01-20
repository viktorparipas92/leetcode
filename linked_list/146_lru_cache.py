"""
146. LRU Cache
-------------------------------
Difficulty: Medium

Implement the Least Recently Used (LRU) cache class LRUCache.
The class should support the following operations
- LRUCache(int capacity): Initialize the LRU cache of size capacity.
- int get(int key): Return the value corresponding to the key if the key exists,
  otherwise return -1.
- void put(int key, int value): Update the value of the key if the key exists.
  Otherwise, add the key-value pair to the cache. If the introduction of the new pair
  causes the cache to exceed its capacity, remove the least recently used key.

A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.

Example 1:
Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

Output:
[null, null, 10, null, null, 20, -1]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20
lRUCache.get(1);      // return -1 (not found)

Constraints:

1 <= capacity <= 100
0 <= key <= 1000
0 <= value <= 1000
"""
from collections import OrderedDict


class LRUCacheBruteForce:
    """
    Time complexity: O(n) for get and put operations.
    Space complexity: O(n) for the cache.
    """
    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i, cache_item in enumerate(self.cache):
            if cache_item[0] == key:
                tmp = self.cache.pop(i)
                self.cache.append(tmp)
                return tmp[1]

        return -1

    def put(self, key: int, value: int) -> None:
        for i, cache_item in enumerate(self.cache):
            if cache_item[0] == key:
                tmp = self.cache.pop(i)
                tmp[1] = value
                self.cache.append(tmp)
                return

        if self.capacity == len(self.cache):
            self.cache.pop(0)

        self.cache.append([key, value])


class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.previous = self.next = None


class LRUCacheDoublyLinkedList:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left: Node = Node(0, 0)
        self.right: Node = Node(0, 0)
        self.left.next, self.right.previous = self.right, self.left

    def remove(self, node):
        previous, next_ = node.previous, node.next
        previous.next, next_.previous = next_, previous

    def insert(self, node):
        previous, next_ = self.right.previous, self.right
        previous.next = next_.previous = node
        node.next, node.previous = next_, previous

    def get(self, key: int) -> int:
        if key in self.cache:
            cached_node = self.cache[key]
            self.remove(cached_node)
            self.insert(cached_node)
            return cached_node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            least_recently_used = self.left.next
            self.remove(least_recently_used)
            del self.cache[least_recently_used.key]


class LRUCache:
    """
    Time complexity: O(1) for get and put operations.
    Space complexity: O(n) for the cache
    """
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


def test_lru_cache():
    solutions = [
        LRUCacheBruteForce,
        LRUCacheDoublyLinkedList,
        LRUCache,
    ]

    for solution in solutions:
        # Arrange
        test_input = [
            'LRUCache', [2],
            'put', [1, 10],
            'get', [1],
            'put', [2, 20],
            'put', [3, 30],
            'get', [2],
            'get', [1],
        ]
        expected_output = [None, 10, None, None, 20, -1]

        # Act
        output = []
        lru_cache = solution(*test_input[1])
        for i in range(2, len(test_input), 2):
            method, args = test_input[i], test_input[i + 1]
            return_value = getattr(lru_cache, method)(*args)
            output.append(return_value)

        # Assert
        assert output == expected_output
        print(f'All tests passed for {solution.__name__}')


if __name__ == '__main__':
    test_lru_cache()