"""
981. Time Based Key-Value Store
------------------------------------------------
Difficulty: Medium
------------------------------------------------
Design a time-based key-value data structure that can store multiple values for
the same key at different time stamps and retrieve the key's value at a certain
timestamp.

Implement the TimeMap class:
- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key key with
  the value value at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was
  called previously, with timestamp_prev <= timestamp.
  If there are multiple such values, it returns the value associated with the
  largest timestamp_prev. If there are no values, it returns "".
"""

class TimeMap:
    def __init__(self):
        self.key_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        result, values = '', self.key_store[key]
        left, right = 0, len(values) - 1
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp:
                result = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1

        return result


def test_time_map():
    instructions = ['set', 'get', 'get', 'set', 'get', 'get']
    inputs = [
        ('foo', 'bar', 1),
        ('foo', 1),
        ('foo', 3),
        ('foo', 'bar2', 4),
        ('foo', 4),
        ('foo', 5),
    ]

    time_map = TimeMap()
    for inputs in zip(instructions, inputs):
        instruction, args = inputs
        if instruction == 'set':
            time_map.set(*args)
        elif instruction == 'get':
            assert time_map.get(*args) == ''