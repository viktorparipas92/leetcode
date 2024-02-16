"""
875. Koko Eating Bananas
-------------------------
Difficulty: Medium

Koko loves to eat bananas. There are n piles of bananas,
the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k.
Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead
and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas
before the guards come back.

Return the minimum integer k such that
she can eat all the bananas within h hours.
"""


def min_eating_speed(piles: list[int], hours: int) -> int:
    left = 1
    right = max(piles)

    while left < right:
        middle = left + (right - left) // 2
        if sum((pile + middle - 1) // middle for pile in piles) > hours:
            left = middle + 1
        else:
            right = middle

    return left


def test_min_eating_speed():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23


if __name__ == '__main__':
    test_min_eating_speed()