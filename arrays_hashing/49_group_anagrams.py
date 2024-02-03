'''
49. Group Anagrams
-------------------
Difficulty: Medium

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.  
'''
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagram_groups = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        anagram_groups[key].append(word)

    return list(anagram_groups.values())


def test_group_anagrams():
    assert (
        group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) ==
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    )
    assert group_anagrams(['']) == [['']]
    assert group_anagrams(['a']) == [['a']]


if __name__ == '__main__':
    test_group_anagrams()