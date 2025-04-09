"""
846. Hand of Straights
-------------------------------
Difficulty: Medium

You are given an integer array hand where hand[i] is the value written on the ith card
and an integer groupSize.

You want to rearrange the cards into groups so that each group is of size groupSize,
and card values are consecutively increasing by 1.

Return true if it's possible to rearrange the cards in this way,
otherwise, return false.

Example 1:
Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4
Output: true
Explanation: The cards can be rearranged as [1,2,3,4] and [2,3,4,5].

Example 2:
Input: hand = [1,2,3,3,4,5,6,7], groupSize = 4
Output: false
Explanation: The closest we can get is [1,2,3,4] and [3,5,6,7],
but the cards in the second group are not consecutive.

Constraints:
1 <= hand.length <= 1000
0 <= hand[i] <= 1000
1 <= groupSize <= hand.length
"""
import heapq
from collections import Counter


def is_n_straight_hand_sorting(hand: list[int], group_size: int) -> bool:
    """
    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    if len(hand) % group_size:
        return False

    count = Counter(hand)
    hand.sort()
    for card in hand:
        if count[card]:
            for i in range(card, card + group_size):
                if not count[i]:
                    return False

                count[i] -= 1

    return True


def is_n_straight_hand_heap(hand: list[int], group_size: int) -> bool:
    """
    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    if len(hand) % group_size:
        return False

    counts = Counter(hand)
    cards = list(counts.keys())
    heapq.heapify(cards)
    while cards:
        first_card = cards[0]
        for card in range(first_card, first_card + group_size):
            if card not in counts:
                return False

            counts[card] -= 1
            if counts[card] == 0:
                if card != cards[0]:
                    return False

                heapq.heappop(cards)

    return True


def test_is_n_straight_hand():
    solutions = [
        is_n_straight_hand_sorting,
        is_n_straight_hand_heap,
    ]

    test_cases = [
        ([1, 2, 4, 2, 3, 5, 3, 4], 4, True),
        ([1, 2, 3, 3, 4, 5, 6, 7], 4, False),
    ]

    for solution in solutions:
        for hand, group_size, expected_is_hand_straight in test_cases:
            # Act
            is_n_straight_hand = solution(hand, group_size)

            # Assert
            assert expected_is_hand_straight == is_n_straight_hand

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_is_n_straight_hand()
    print('All tests passed!')
