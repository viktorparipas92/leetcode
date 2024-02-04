"""
238. Product of Array Except Self
---------------------------------
Difficulty: Medium

Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""


def product_except_self(nums: list[int]) -> list[int]:
    length = len(nums)
    products = [1] * length
    for i in range(1, length):
        products[i] = products[i-1] * nums[i-1]
    # products = [1, 1, 2, 6]

    right = nums[-1] # 4
    for i in range(length - 2, -1, -1): # 2, 1, 0
        products[i] *= right  # 2 * 4, 1 * 12, 1 * 24
        right *= nums[i]  # 4 * 3, 12 * 2, 24 * 1

    return products


def test_product_except_self():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


if __name__ == '__main__':
    test_product_except_self()