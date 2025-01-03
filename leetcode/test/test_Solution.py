from leetcode.top_k_frequent_elements.Solution import Solution
import pytest


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

    assert Solution().topKFrequent(nums, k) == expected
