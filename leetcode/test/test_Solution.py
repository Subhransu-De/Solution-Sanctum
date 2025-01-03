import pytest
from leetcode.top_k_frequent_elements.Solution import (
    Solution as solution_top_k_frequent,
)
from leetcode.roman_to_integer.Solution import Solution as solution_roman_to_integer


@pytest.mark.parametrize(
    "test_input",
    [
        {"nums": [1, 1, 1, 2, 2, 3], "k": 2, "expected": [1, 2]},
        {"nums": [1], "k": 1, "expected": [1]},
        {"nums": [1, 2], "k": 2, "expected": [1, 2]},
    ],
)
def test_top_k_frequent(test_input):
    nums = test_input["nums"]
    k = test_input["k"]
    expected = test_input["expected"]

    assert solution_top_k_frequent().topKFrequent(nums, k) == expected


@pytest.mark.parametrize(
    "test_input",
    [
        {"s": "III", "expected": 3},
        {"s": "LVIII", "expected": 58},
        {"s": "MCMXCIV", "expected": 1994},
        {"s": "IV", "expected": 4},
        {"s": "IX", "expected": 9},
        {"s": "XL", "expected": 40},
        {"s": "XC", "expected": 90},
        {"s": "CD", "expected": 400},
        {"s": "CM", "expected": 900},
    ],
)
def test_roman_to_int(test_input):
    s = test_input["s"]
    expected = test_input["expected"]

    assert solution_roman_to_integer().romanToInt(s) == expected
