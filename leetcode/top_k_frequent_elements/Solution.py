# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [most_common[0] for most_common in Counter(nums).most_common(k)]
