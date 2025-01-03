# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        prev = 0
        for char in s:
            current = roman_to_int[char]
            if current > prev:
                result += current - 2 * prev
            else:
                result += current
            prev = current
        return result
