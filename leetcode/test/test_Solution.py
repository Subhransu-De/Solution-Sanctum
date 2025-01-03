from leetcode.top_k_frequent_elements.Solution import Solution
import pytest

@pytest.mark.benchmark(max_time=0.100)
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([1, 2], 2, [1, 2]),
    ],
)
def test_top_k_frequent(benchmark, nums, k, expected):
    solution = Solution()
    assert benchmark(solution.topKFrequent, nums, k) == expected
